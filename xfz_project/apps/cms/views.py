from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View

from django.views.decorators.http import require_POST, require_GET
from apps.news.models import NewCategory
from utils import restful
from .forms import EditNewsCategory
import os
from django.conf import settings
import qiniu


def login_view(request):
    return render(request, 'cms/login.html')


@staff_member_required(login_url='index')
def index(request):
    return render(request, 'cms/index.html')


class WriteNewView(View):
    def get(self, request):
        categories = NewCategory.objects.all()
        context = {'categories': categories}
        return render(request, 'cms/write_news.html', context=context)


@require_GET
def news_category(request):
    categories = NewCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'cms/news_category.html', context=context)


@require_POST
def add_news_category(request):
    name = request.POST.get('name')
    exists = NewCategory.objects.filter(name=name).exists()
    if not exists:
        NewCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message="该分类已经存在")


@require_POST
def edit_news_category(request):
    form = EditNewsCategory(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            NewCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message="该分类不存在")
    else:
        return restful.params_error(message=form.get_error())


@require_POST
def delete_news_category(request):
    pk = request.POST.get('pk')
    try:
        NewCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message="该分类不存在")


@require_POST
def upload_file(request):
    file = request.FILES.get('file')
    name = file.name
    with open(os.path.join(settings.MEDIA_ROOT, name), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = request.build_absolute_uri(settings.MEDIA_URL + name)
    return restful.result(data={'url': url})


@require_GET
def qntoken(request):
    access_key = 'XfppOEavIJgP8xTCDttLhQDbGoGlsUA7L6LzNMKv'
    secret_key = '3CauEK3LPIoJcATC2URnLSmg6yOMJjiqDPSyPlDX'

    bucket = 'hyvideopx'
    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(bucket)

    return restful.result(data={'token': token})

