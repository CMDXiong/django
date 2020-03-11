from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import MyUser, Article
from django.contrib.auth import authenticate
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, ContentType, Group


def inherit_view(request):
    telephone = '17788889999'
    password = '111111'
    email = '123@qq.com'
    username = 'px'
    user = MyUser.objects.create_user(telephone=telephone, username=username,
                                      password=password, email=email)
    print(user.username)
    return HttpResponse('继承AbstracterUser扩展用户')


def authen(request):
    telephone = '17788889999'
    password = '111111'
    user = authenticate(request, username=telephone, password=password)
    if user:
        print(user.username)
    return HttpResponse('继承AbstracterUser扩展用户的验证')


# 登录
def my_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, username=telephone, password=password)
            if user and user.is_active:
                login(request, user)
                if remember:
                    # 设置为None, 则表示使用全局的过期时间
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse("登录成功")
            else:
                return HttpResponse('手机号或者密码错误')
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))


# 登出
def my_logout(request):
    logout(request)
    return HttpResponse('成功退出')

# 个人信息页面
@login_required(login_url='/login/')
def profile(request):
    return HttpResponse("这是个人中心，只有登录了以后才能查看到")


def create_permission(request):
    content_type = ContentType.objects.get_for_model(Article)
    permission = Permission.objects.create(name="拉黑文章", content_type=content_type, codename='black_article')
    return HttpResponse("权限创建成功")


def operation_permission(request):
    user = MyUser.objects.first()
    content_type = ContentType.objects.get_for_model(Article)
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        print(permission)
    # 1. 给user绑定权限
    user.user_permissions.set(permissions)
    # 2. 删除user的权限
    user.user_permissions.clear()
    # 3 一个个添加权限
    user.user_permissions.add(*permissions)
    # 4. 一个个删除权限
    # user.user_permissions.remove(*permissions)
    # 5. 判断是否拥有某个权限
    if user.has_perm('front.view_article'):
        print('拥有front.view_article权限')
    else:
        print("没有front.view_article权限")
    # 6. 获取所有的权限
    print(user.get_all_permissions())
    return HttpResponse("操作权限")


def add_article(request):
    if request.user.is_authenticated:
        print('已经登录了')
        if request.user.has_perm('front.add_article'):
            return HttpResponse("添加文章的页面")
        else:
            return HttpResponse("没有权限", status=403)
    else:
        redirect(reverse('login'))


def operator_group(request):
    # 1. 新建一个分组
    # group = Group.objects.create(name='运营')
    # content_type = ContentType.objects.get_for_model(Article)
    # permissions = Permission.objects.filter(content_type=content_type)
    # group.permissions.set(permissions)
    # group.save()

    group = Group.objects.filter(name='运营').first()
    user = MyUser.objects.first()
    # 2. 添加分组
    user.groups.add(group)
    user.save()

    # 获取分组下的所有权限
    user.get_group_permissions()

    # user.has_perm()
    # 先判断自身有没有，再判断组有没有
    return HttpResponse("操作分组")
