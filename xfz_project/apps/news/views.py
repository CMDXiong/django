from django.shortcuts import render
from django.http import HttpResponse
from .models import News, NewCategory
from django.conf import settings
from utils import restful
from .serializers import NewsSerializer
from django.http import Http404


def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    # newses = News.objects.all()[0:count]
    # 优化
    newses = News.objects.select_related('category', 'author').all()[0:count]
    cateories = NewCategory.objects.all()
    context = {
        'newses': newses,
        'categories': cateories
    }
    return render(request, 'news/index.html', context=context)


def news_list(request):
    # 通过参数p，来指定要获取第几页的数据
    page = int(request.GET.get('p', 1))

    # 分类为0，代表不进行任何分类，直接按照时间倒序排序
    category_id = int(request.GET.get('category_id', 0))
    start = (page - 1) * settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.select_related('category', 'author').all()[start: end]
    else:
        newses = News.objects.select_related('category', 'author').filter(category__id=category_id)[start: end]

    serializer = NewsSerializer(newses, many=True)
    data = serializer.data

    return restful.result(data=data)


def news_detail(request, news_id):
    try:
        news = News.objects.select_related('category', 'author').get(pk=news_id)
        context = {
            "news": news
        }
        return render(request, 'news/news_detail.html', context=context)
    except:
        raise Http404


def search(request):
    return render(request, 'search/search.html')


