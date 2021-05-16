from django.shortcuts import render

from django.http import JsonResponse
from hello_friend_db_api.models import *
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def getAllUsers(request):
    if request.method == 'GET':
        try:
            users = User.nodes.all()
            response = []
            logging.info("Executing getAllUsers method...")
            for user in users :
                obj = {
                    "uid": user.uid,
                    "name": user.name,
                    "age": user.age,
                    "gender": user.gender,
                    "email": user.email,
                    "interests": user.interests,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing getAllUsers method...")
            return JsonResponse(response, safe=False)

@csrf_exempt
def userSimilarity(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email = json_data['email']
        try:
            user_current = User.nodes.get(email=email)
            users = User.nodes.all()
            response = []
            similarity = dict()
            logging.info("Executing Similar Users method...")
            for user in users:
                if user.uid != user_current.uid:
                    sim, common_interest = User.getSimilarityWithInterests(user_current.interests, user.interests)
                    obj = {
                        "uid": user.uid,
                        "name": user.name,
                        "age": user.age,
                        "gender": user.gender,
                        "email": user.email,
                        "interests": user.interests,
                        "similarity_score": sim,
                        "common_interests": list(common_interest)
                    }
                    similarity[(sim, user.uid)] = obj
            similarity_keys = list(similarity.keys())
            similarity_keys.sort(reverse=True)
            for key in similarity_keys:
                response.append(similarity[key])
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing similar users method...")
            return JsonResponse(response, safe=False)

    if request.method == 'GET':
        json_data = json.loads(request.body)
        name1 = json_data['name1']
        name2 = json_data['name2']
        try:
            logging.info("Executing userDetails GET method...")
            sim, common_interest = User.getSimilarity(name1, name2)
            response = {
                "similarity_score": sim,
                "common_interests": list(common_interest)
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing userDetails GET method...")
            return JsonResponse(response, safe=False)

@csrf_exempt
def checkLogin(request):
    if request.method == 'POST':
        # print(request.body)
        json_data = json.loads(request.body)
        password = json_data['password']
        email = json_data['email']
        try:
            user = User.nodes.get(email=email)
            if (user.password == password):
                response = {
                    "validLogin": 'True',
                    "uid": user.uid,
                    "name": user.name,
                    "age": user.age,
                    "gender": user.gender,
                    "email": user.email,
                    "interests": user.interests,
                }
                return JsonResponse(response, safe=False)
            else:
                response = {
                    "validLogin": 'False'
                }
                return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing checkLogin GET method...")
            return JsonResponse(response, safe=False)

@csrf_exempt
def userDetails(request):
    if request.method == 'GET':
        json_data = json.loads(request.body)
        email = json_data['email']
        try:
            logging.info("Executing userDetails GET method...")
            user = User.nodes.get(email=email)
            response = {
                "uid": user.uid,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
                "email": user.email,
                "interests": user.interests,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing userDetails GET method...")
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one user
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        gender = json_data['gender']
        password = json_data['password']
        email = json_data['email']
        interests = json_data['interests']
        interests = [interest['label'] for interest in interests]
        try:
            logging.info("Executing userDetails POST method...")
            user = User(name=name, age=age, gender=gender, password=password, email=email, interests=interests)
            user.save()
            for interest in interests:
                interest_node = None
                try:
                    interest_node = Interest.nodes.get(name=interest['label'])
                except:
                    interest_node = Interest(name=interest['label'])
                    interest_node.save()
                user.interestedIn.connect(interest_node)
            user.save()
            response = {
                "uid": user.uid,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
                "email": user.email,
                "interests": user.interests,
            }
            return JsonResponse(response)
        except:
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing userDetails POST method...")
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one user
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        gender = json_data['gender']
        password = json_data['password']
        email = json_data['email']
        interests = json_data['interests']
        interests = [interest['label'] for interest in interests]
        uid = json_data['uid']
        try:
            logging.info("Executing userDetails PUT method...")
            user = User.nodes.get(uid=uid)
            user.name = name
            user.age = age
            user.gender = gender
            user.email = email
            user.interests = interests
            user.password = password
            user.interestedIn.disconnect_all()
            for interest in interests:
                interest_node = None
                try:
                    interest_node = Interest.nodes.get(name=interest['label'])
                except:
                    interest_node = Interest(name=interest['label'])
                    interest_node.save()
                user.interestedIn.connect(interest_node)
            user.save()
            response = {
                "uid": user.uid,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing userDetails PUT method...")
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one user
        json_data = json.loads(request.body)
        uid = json_data['uid']
        try:
            logging.info("Executing userDetails DELETE method...")
            user = User.nodes.get(uid=uid)
            user.delete()
            response = {"success": "User deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            logging.error("Error occured while executing userDetails DELETE method...")
            return JsonResponse(response, safe=False)
