from django.conf.urls import url
from hello_friend_db_api.views import *
from django.urls import path

urlpatterns = [
    path('user', userDetails),
    path('login', checkLogin),
    path('similarity', userSimilarity),
    path('getAllUsers', getAllUsers),
    path('connectUaU',connectUaU),
]