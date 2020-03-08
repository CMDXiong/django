"""form_demo URL Configuration

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
from django.urls import path, include
from front import views

urlpatterns = [
    path('', views.IndexView.as_view()),  # django表单渲染功能示例
    path('index1/', views.Index1View.as_view(), name='index1'),  # django验证器示例
    path('register/', views.RegisterView.as_view(), name='register'),  # 自定义验证示例

    # ModelForm示例
    path('modelform/', include('modelform_demo.urls', namespace='modelform')),
    # uploadfile示例
    path('uploadfile/', include('uploadfile_demo.urls', namespace='uploadfile')),
]
