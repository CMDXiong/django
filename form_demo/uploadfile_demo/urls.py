from django.urls import path, include
from uploadfile_demo import views

app_name = 'uploadfile_demo'

urlpatterns = [
    path('', views.IndexView.as_view()),
    # path('add_book/', views.AddBookView.as_view()),  # django表单渲染功能示例
    # path('register/', views.RegisterView.as_view()),  # django表单渲染功能示例
]