from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Article


class IndexView(View):
    def get(self, request):
        return render(request, 'uploadfile/index.html')

    # 普通上传文件 方式
    # def post(self, request):
    #     myfile = request.FILES.get('myfile')
    #     with open('somefile.txt', 'wb') as fp:
    #         for chunk in myfile.chunks():
    #             fp.write(chunk)
    #         return HttpResponse('uploadfile success')

    # 使用模型来自动处理上传的文件和获取上传文件url
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('myfile')
        Article.objects.create(title=title, content=content, thumbnial=file)
        return HttpResponse('uploadfile success')

