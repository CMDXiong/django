# -*- coding:utf-8 -*-
__author__ = 'px'

from django.urls import path
from . import views

# 有了app_name，以后出现相同命名的url时，可以用app_name进行区分
app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
]

