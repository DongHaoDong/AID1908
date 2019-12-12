from django.http import JsonResponse
from django.shortcuts import render
import json
import jwt

# Create your views here.


def users(request):

    if request.method == 'GET':
        # 获取用户数据
        return JsonResponse({'code': 200})

    elif request.method == 'POST':
        # 此功能模块的异常码从201开始
        # request.POST 只能拿表单post提交数据
        # 创建用户
        # 前端注册页面地址 http://127.0.0.1:5000/register
        # user_dict = json.loads(request.body)
        # import jwt
        # jwt.encode
        return JsonResponse({'code':200,'username':'donghaodong','data':{'token':'abcdef'}})

    elif request.method == 'PUT':
        # 更新数据
        pass
    else:
        raise
    return JsonResponse({'code':200})
