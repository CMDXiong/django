# -*- coding:utf-8 -*-
__author__ = 'px'
from .models import User


def front_user(request):
    context = {}
    try:
        user_id = request.session['user_id']
        user = User.objects.get(pk=user_id)
        context['front_user'] = user
    except:
        pass

    return context
