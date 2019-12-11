import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def load_test(request):
    return render(request,'load_test.html')


def load_test_server(request):
    return render(request,'load_test_server.html')


def jquery_get(request):
    return render(request,'jquery_get.html')


def jquery_get_server(request):
    username = request.GET.get("username",'username meizhaodao')
    age = request.GET.get("age",'age meizhaodao')
    data = {'username':username,'age':age}
    return HttpResponse(json.dumps(data),content_type='application/json')


def jquery_post(request):
    return render(request,'jquery_post.html')


def jquery_post_server(request):
    if int(request.POST.get('age',0)) > 100:
        data = {"msg":"Your age is big!","code":202}
        return HttpResponse(json.dumps(data),content_type="application/json")
    data = {"msg":"post is ok",'code':200}
    return HttpResponse(json.dumps(data),content_type="application/json")


def jquery_ajax(request):
    return render(request, 'jquery_ajax.html')


def jquery_ajax_server(request):
    data = {"name":"donghaodong","age":21}
    return HttpResponse(json.dumps(data),content_type="application/json")


def jquery_ajax_user(request):
    return render(request,'jquery_ajax_user.html')


def jquery_ajax_user_server(request):
    data = [
        {'name':"董浩东",'age':21},
        {'name':"刘凡",'age':24},
        {'name':"张乐乐",'age':23},
        {'name':"陈欢",'age':23},
        {'name':"杨悦悦",'age':22},
        {'name':"薛辰",'age':21}
    ]
    return HttpResponse(json.dumps(data), content_type="application/json")


def cross(request):
    return render(request,'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    # print
    return HttpResponse(func + "('wo kua chu lai le hahaha')")


def cross_server_json(request):
    func = request.GET.get('callback')
    data = {"name":"dongghaodong","age":21}
    return HttpResponse(func+"("+json.dumps(data)+")")