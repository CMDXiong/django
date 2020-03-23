from django.shortcuts import render
from django.http import HttpResponse
from .models import News, NewCategory
from django.conf import settings
from utils import restful
from .serializers import NewsSerializer


def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.order_by('-pub_time')[0:count]
    cateories = NewCategory.objects.all()
    context = {
        'newses': newses,
        'categories': cateories
    }
    return render(request, 'news/index.html', context=context)


def news_list(request):
    # 通过参数p，来指定要获取第几页的数据
    page = int(request.GET.get('p', 1))
    start = (page - 1) * settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.order_by('-pub_time')[start: end]
    serializer = NewsSerializer(newses, many=True)
    data = serializer.data

    return restful.result(data=data)


def news_detail(request, news_id):
    return render(request, 'news/news_detail.html')


def search(request):
    return render(request, 'search/search.html')


