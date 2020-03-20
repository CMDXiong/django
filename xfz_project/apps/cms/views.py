from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View


def login_view(request):
    return render(request, 'cms/login.html')


@staff_member_required(login_url='index')
def index(request):
    return render(request, 'cms/index.html')


class WriteNewView(View):
    def get(self, request):
        return render(request, 'cms/write_news.html')

