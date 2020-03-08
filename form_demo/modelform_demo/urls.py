from django.urls import path, include
from modelform_demo import views

app_name = 'modelform_demo'

urlpatterns = [
    path('', views.index),
    path('add_book/', views.AddBookView.as_view()),  # django表单渲染功能示例
    path('register/', views.RegisterView.as_view()),  # django表单渲染功能示例
]