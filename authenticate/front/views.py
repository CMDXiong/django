from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
    # 1. 创建用户
    # User.objects.create_user(username='px', email='1357@qq.com', password='123')

    # 2. 创建超级用户
    # User.objects.create_superuser(username='super_px', email='1357@qq.com', password='123')

    # 3. 修改密码
    # user = User.objects.get(pk=1)
    # 不能使用user.password = '222222'修改密码
    # user.set_password('222222')

    # 4. 登录验证
    username = 'px'
    password = '123'
    user = authenticate(request, username=username, password=password)
    if user:
        print('登录成功', user.username)
    else:
        print('用户名或者密码错误')

    return HttpResponse('success')


from .models import Person
def proxy_view(request):
    blacklist = Person.get_blacklist()
    for person in blacklist:
        print(person.username)
    return HttpResponse('proxy')


def one_veiw(request):
    telephone = '18888888888'
    user = my_authenticate(telephone, password='111111')
    print(user.username)
    # user = User.objects.create_user(username='px2', email='123@qq.com', password='111111')
    return HttpResponse("一对一扩展模型")


def my_authenticate(telephone, password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None