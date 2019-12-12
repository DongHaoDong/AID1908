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
        json_str = request.body
        if not json_str:
            result = {'code':201,'error':'Please give me data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        if not username:
            result = {'code':202,'error':"Please give me username"}
            return JsonResponse(result)
        email = json_obj.get('email')
        if not email:
            result = {'code':203,'error':"Please give me email"}
            return JsonResponse(result)
        password_1 = json_obj.get('password_1')
        password_2 = json_obj.get('password_2')
        if not password_1 or not password_2:
            result = {'code': 204, 'error': "Please give me password"}
            return JsonResponse(result)
        if password_1 != password_2:
            result = {'code': 205, 'error': "Your password not same"}
            return JsonResponse(result)
        return JsonResponse({'code':200,'username':'donghaodong','data':{'token':'abcdef'}})

    elif request.method == 'PUT':
        # 更新数据
        pass
    else:
        raise
    return JsonResponse({'code':200})
