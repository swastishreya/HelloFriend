from django.shortcuts import render

from django.http import JsonResponse
from hello_friend_db_api.models import User
from django.views.decorators.csrf import csrf_exempt
import json


def getAllUsers(request):
    if request.method == 'GET':
        try:
            users = User.nodes.all()
            response = []
            for user in users :
                obj = {
                    "uid": user.uid,
                    "name": user.name,
                    "age": user.age,
                    "gender": user.gender,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def userDetails(request):
    if request.method == 'GET':
        # get one user by name
        name = request.GET.get('name', ' ')
        try:
            user = User.nodes.get(name=name)
            response = {
                "uid": user.uid,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one user
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        gender = json_data['gender']
        try:
            user = User(name=name, age=age, gender=gender)
            user.save()
            response = {
                "uid": user.uid,
                "name": user.name,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one user
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        gender = json_data['gender']
        uid = json_data['uid']
        try:
            user = User.nodes.get(uid=uid)
            user.name = name
            user.age = age
            user.gender = gender
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
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one user
        json_data = json.loads(request.body)
        uid = json_data['uid']
        try:
            user = User.nodes.get(uid=uid)
            user.delete()
            response = {"success": "User deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
