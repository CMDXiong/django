# -*- coding:utf-8 -*-
__author__ = 'px'
from .models import User


def front_user_middleware(get_response):
    # 执行一些初始化代码,只会执行一次，django项目启动后，执行一次就不再执行
    print('front_user_middleware中间件初始化的代码')

    def middleware(request):
        print('request到过view之前执行的代码...')
        # 在这里写request到view之前执行的代码...
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None

        response = get_response(request)
        print('response到浏览器之前执行的代码...')
        # 在这里写response到浏览器之前执行的代码...
        return response

    return middleware


class FrontUserMiddleware(object):
    def __init__(self, get_response):
        # 执行一些初始化代码,只会执行一次，django项目启动后，执行一次就不再执行
        print('front_user_middleware中间件初始化的代码')
        self.get_response = get_response

    def __call__(self, request):
        print('request到过view之前执行的代码...')
        # 在这里写request到view之前执行的代码...
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None

        response = self.get_response(request)
        print('response到浏览器之前执行的代码...')
        # 在这里写response到浏览器之前执行的代码...
        return response


from django.utils.deprecation import MiddlewareMixin


class FrontUserMiddlewareMixin(MiddlewareMixin):
    def __init__(self, get_response):
        # 执行一些初始化代码,只会执行一次，django项目启动后，执行一次就不再执行
        print('front_user_middleware中间件初始化的代码')
        super(FrontUserMiddlewareMixin, self).__init__(get_response)

    # 在这里写request到view之前执行的代码...
    def process_request(self, request):
        print('request到过view之前执行的代码...')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None

    # 在这里写response到浏览器之前执行的代码...
    def process_response(self, request, response):
        print('response到浏览器之前执行的代码...')
        return response

