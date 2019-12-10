from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .models import User


def xhr(request):
    return render(request,'xhr.html')


def get_xhr(request):
    return render(request,'get-xhr.html')


def get_xhr_server(request):
    if request.GET.get('username'):
        username = request.GET['username']
        return HttpResponse("welcome %s"%(username))
    return HttpResponse("This is ajax request")


def register(request):
    return render(request,'register.html')


def checkname(request):
    # 获取ajax传过来的用户名
    username = request.GET.get('username')
    # 校验用户名是否存在
    users = User.objects.filter(username=username)
    if users:
        return HttpResponse("1")
    return HttpResponse("0")


def make_post(request):
    if request.method == 'GET':
        return render(request,'make_post.html')
    elif request.method == 'POST':
        # 获取表单数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse('Your post is ok!!')
    else:
        raise