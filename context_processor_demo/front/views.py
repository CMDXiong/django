from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import SignupForm, SigninForm
from .models import User


def index(request):
    # 将认证的部分写到上下文处理器中
    # user_id = request.session['user_id']
    # context = {}
    # try:
    #     user = User.objects.get(pk=user_id)
    #     context['front_user'] = user
    # except:
    #     pass

    # return render(request, 'index.html', context=context)
    return render(request, 'index.html')


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                print('用户名或者密码错误')
                return redirect(reverse('signin'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signin'))


class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            errors = form.errors.get_json_data()
            print(errors)
            return redirect(reverse('signup'))


def blog(request):
    return render(request, 'blog.html')


def video(request):
    return render(request, 'video.html')

