# -*- coding:utf-8 -*-
__author__ = 'px'
from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    paramerror = 400
    unauth = 401
    methoderror = 405
    servererror = 500


def result(code=HttpCode.ok, message="", data=None, kwargs=None):
    json_dict = {"code": code, "message": message, "data": data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)


def ok(message="", data=None):
    return result(code=HttpCode.ok, message=message, data=data)


def params_error(message="", data=None):
    return result(code=HttpCode.paramerror, message=message, data=data)


def unauth(message="", data=None):
    return result(code=HttpCode.unauth, message=message, data=data)


def method_error(message="", data=None):
    return result(code=HttpCode.methoderror, message=message, data=data)


def servere_error(message="", data=None):
    return result(code=HttpCode.servererror, message=message, data=data)

