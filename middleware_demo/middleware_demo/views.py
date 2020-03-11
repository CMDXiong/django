# -*- coding:utf-8 -*-
__author__ = 'px'

from django.http import HttpResponse


def index(request):
    return HttpResponse('success')
