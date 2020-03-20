# -*- coding:utf-8 -*-
__author__ = 'px'


from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('write_news/', views.WriteNewView.as_view(), name='write_news'),
]
