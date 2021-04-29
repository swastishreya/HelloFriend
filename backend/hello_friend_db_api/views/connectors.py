from django.http import JsonResponse
from hello_friend_db_api.models import *
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def connectUaU(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        uid1 = json_data['uid1']
        uid2 = json_data['uid2']
        try:
            user1 = User.nodes.get(uid=uid1)
            user2 = User.nodes.get(uid=uid2)
            res = user1.friends.connect(user2)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)