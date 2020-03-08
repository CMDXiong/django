from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm, RegisterForm
from django.views.generic import View


def index(request):
    return HttpResponse("ModelForm Index")


class AddBookView(View):
    def get(self, request):
        return render(request, 'modelform_demo.html')

    def post(self, request):
        form = AddBookForm(request.POST)
        print(request.POST.get('page'))
        if form.is_valid():
            title = form.cleaned_data.get('title')
            page = form.cleaned_data.get('page')
            price = form.cleaned_data.get('price')
            print(title, page, price)
            form.save()  # 保存到数据库中
            return HttpResponse("add book success")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("add book fail")


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data.get('pwd1')
            user.save()
            return HttpResponse("注册成功")
        else:
            print(form.errors.get_json_data())
            return HttpResponse('注册失败')
