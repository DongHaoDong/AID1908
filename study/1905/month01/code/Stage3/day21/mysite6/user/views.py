from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.


def reg_view(request):
    if request.method == 'GET':
        return render(request,'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        # 验证数据的合法性
        if len(username) < 6:
            username_error = '用户名太短!'
            return render(request,'user/register.html',locals())
        # 验证密码1不能为空
        if len(password) == 0:
            password_error = "密码不能为空!"
            return render(request, 'user/register.html', locals())
        # 验证两次密码必须一致
        if password != password2:
            password2_error = "两次密码不一致!"
            return render(request, 'user/register.html', locals())
        # 检查数据库是否已有username这条记录，如果没有完成注册
        try:
            user = User.objects.get(username=username)
            username_error = "用户名已经存在!"
            return render(request,'user/register.html',locals())
        except:
            # user = User.objects.create_user(username=username,password=password)
            user = User.objects.create_superuser(username=username,password=password,email='584023982@qq.com')
        # try:
        #     user = models.User.objects.get(username=username)
        #     username_error = "用户名已经存在!"
        #     return render(request,'user/register.html',locals())
        # except:
        #     user = models.User.objects.create(username=username,password=password)
            html = "注册成功!<a href='/user/login'>进入登录</a>"
            # 添加co0kies
            response = HttpResponse(html)
            response.set_cookie("username",username)
            return response


def login_view(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username','')
        return render(request,'user/login.html',locals())
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == '':
            username_error = "用户名不能为空"
            return render(request,'user/login.html',locals())
        # 处理登录的逻辑
        try:
            user = User.objects.get(
                username=username
            )
            if user.check_password(password):
                # 记录一个登录状态
                request.session['user'] = {
                    'username':username,
                    'id':user.id    # 记录当前用户的id
                }
                response = HttpResponseRedirect('/')
                if 'remember' in request.POST:  # 选中状态
                    response.set_cookie('username',username)
                return response
                # return HttpResponse("登陆成功")
            else:
                password_error = "密码错误"
                return render(request,'user/login.html',locals())
        except:
            password_error = "用户名或密码不正确"
            return render(request,'user/login.html',locals())
        # try:
        #     user = models.User.objects.get(
        #         username=username,password=password
        #     )
        #     # 记录一个登录状态
        #     request.session['user'] = {
        #         'username':username,
        #         'id':user.id    # 记录当前用户的id
        #     }
        #     response = HttpResponseRedirect('/')
        #     if 'remember' in request.POST:  # 选中状态
        #         response.set_cookie('username',username)
        #     return response
        #     # return HttpResponse("登陆成功")
        # except:
        #     password_error = "用户名或密码不正确"
        #     return render(request,'user/login.html',locals())


def logout_view(request):
    '''退出登录'''
    if 'user' in request.session:
        del request.session['user']    # 清除登录记录
    return HttpResponseRedirect('/')    # 返回主页


from . import forms


def register_view(request):
    if request.method == 'GET':
        myform = forms.MyRegForm()
        return render(request,'user/reg.html',locals())
    elif request.method == 'POST':
        myform = forms.MyRegForm(request.POST)
        if myform.is_valid():
            dic = myform.changed_data
            username = dic['username']
            password = dic['password']
            password2 = dic['password2']
            return HttpResponse(str(dic))
        else:
            return HttpResponse("表单验证失败")

