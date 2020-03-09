from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUser
from django.contrib.auth import authenticate

def inherit_view(request):
    telephone = '17788889999'
    password = '111111'
    username = 'px'
    user = MyUser.objects.create_user(telephone=telephone, username=username,
                                      password=password)
    print(user.username)
    return HttpResponse('继承AbstracterUser扩展用户')


def authen(request):
    telephone = '17788889999'
    password = '111111'
    user = authenticate(request, username=telephone,password=password)
    if user:
        print(user.username)
    return HttpResponse('继承AbstracterUser扩展用户的验证')