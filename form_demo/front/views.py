from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm, MyForm, RegisterForm
from django.http import HttpResponse
from django.forms.utils import ErrorDict
from .models import User


# django表单渲染功能示例
class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', context={"form": form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            # 通过dango后，price是浮点型
            # request.POST.get('price')得到的是字符串
            price = form.cleaned_data.get('price')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print(title, price, content, email, reply)
            return HttpResponse('success')
        else:
            print(form.errors)
            print(form.errors.get_json_data())
            return HttpResponse('fail')


# django验证器示例
class Index1View(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'index.html', context={"form": form})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            return HttpResponse('success')
        else:
            print(form.errors)
            print(form.errors.get_json_data())
            return HttpResponse('fail')


# 自定义验证示例
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            telephone
            User.objects.create(username=username, telephone=telephone)
            return HttpResponse("注册成功")
        else:
            print(form.get_errors())
            return HttpResponse('注册失败')

