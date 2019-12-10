from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.


def index_view(request):
    print("主页被访问！")
    return HttpResponse("主页")


def page1_view(request):
    raise Http404
    # return HttpResponse("页面1")
