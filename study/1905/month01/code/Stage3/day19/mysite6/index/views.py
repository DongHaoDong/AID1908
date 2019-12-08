from django.shortcuts import render

# Create your views here.
# file:index/views.py


def index_view(request):
    return render(request,'index/index.html',locals())


from django.http import HttpResponse


def test_view(request):
    print('test_view被调用')
    return HttpResponse("请求到达了/test页面")
