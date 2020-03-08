from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    response = HttpResponse('index')
    expires = datetime(year=2020, month=3, day=9, hour=23, minute=30, second=0)
    expires = make_aware(expires)
    response.set_cookie('username', 'px', max_age=60, expires=expires,
                        path='/')
    response.set_cookie('user_id', 'px1', max_age=60, expires=expires,
                        path='/cms/')
    return response


def my_list(request):
    cooike = request.COOKIES
    username = cooike.get('username')
    return HttpResponse(username)


def cms(request):
    cooike = request.COOKIES
    user_id = cooike.get('user_id')
    return HttpResponse(user_id)


def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('username')
    return response


# 设置session
def session_view(request):
    request.session['username'] = 'px'
    request.session['user_id'] = 111
    request.session.set_expiry(0)
    return HttpResponse('session view')


# 操作session
def man_session(request):
    # username = request.session.get('username')
    username = request.session.pop('username')
    request.session.clear()  # sessionid还存在
    request.session.flush()  # sessionid还存在
    request.session.clear_expired()
    print(username)
    return HttpResponse('man session')

