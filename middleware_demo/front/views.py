from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import SignupForm, SigninForm
from .models import User
from django.contrib import messages


def index(request):
    if request.front_user:
        print(request.front_user.username)
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
                # 以下两种都可以
                # messages.add_message(request, messages.INFO, '用户名或者密码错误')
                messages.info(request, '用户名或者密码错误')
                return redirect(reverse('signin'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signin'))

