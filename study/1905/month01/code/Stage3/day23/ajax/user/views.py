from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


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
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        # register
        username = request.POST.get('username')
        if not username:
            return HttpResponse("请输入用户名")
        password = request.POST.get('password')
        if not password:
            return HttpResponse("请输入密码")
        nickname = request.POST.get('nickname')
        if not nickname:
            return HttpResponse("请输入昵称")
        try:
            User.objects.create(username=username,password=password,nickname=nickname)
        except Exception as e:
            return HttpResponse('注册失败，请稍后重试')
        return HttpResponse('注册成功')


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


def get_user(request):
    return render(request,'get_user.html')


def get_user_server(request):
    users = User.objects.all()
    data = ''
    for user in users:
        data += '%s_%s_%s|'%(user.username,user.password,user.nickname)
    last_data = data[0:-1]
    return HttpResponse(last_data)


def json_object(request):
    return render(request,'json_object.html')


def json_dumps(request):
    # 1. 生成单个对象的json字符串/序列化 - obj - str
    # 反序列化 - str -> obj
    dic = {
        "username":"Lili",
        "age":"30"
    }
    # sort_keys让输出的json有序
    # separators:参数(',',':')第一个参数是指每一个键值对之间用当前参数分割;第二个参数是指每个键值对中的键和值之间用当前参数分隔
    json_str = json.dumps(dic,sort_keys=True,separators=(',',':'))
    # 2. 生成多个对象的json字符串
    s = [
        {
            "username":"lili",
            "age":18,
        },
        {
            "username":"panghu",
            "age":21,
        }
    ]
    json_str_arr=json.dumps(s)
    # django v1
    # from django.core import serializers
    # users = User.objects.all()
    # json_str_all = serializers.serialize('json',users)
    # return HttpResponse(json_str_all,content_type="application/json")

    # [{}]
    # l = []
    # users = User.objects.all()
    # for user in users:
    #     d = {}
    #     d['username'] = user.username
    #     d['password'] = user.password
    #     d['nickname'] = user.nickname
    #     l.append(d)
    # all_json=json.dumps(l)
    return HttpResponse(json_str_arr,content_type="application/json")
    # django v2
    # return JsonResponse(dic)