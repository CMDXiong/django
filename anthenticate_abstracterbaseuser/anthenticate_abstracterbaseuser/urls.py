"""anthenticate_abstracterbaseuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inherit/', views.inherit_view),
    path('auth/', views.authen),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_permission/', views.create_permission, name='create_permission'),
    path('operation_permission/', views.operation_permission, name='operation_permission'),
    path('article/', views.add_article, name='article'),
    path('group/', views.operator_group, name='group'),
]
