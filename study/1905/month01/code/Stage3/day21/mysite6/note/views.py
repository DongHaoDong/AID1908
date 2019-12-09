from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from user.models import User
from django.core.paginator import Paginator
from . import models
# Create your views here.


def check_login(fn):
    def warp(request,*args,**kwargs):
        if not hasattr(request, 'session'):
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request,*args,**kwargs)
    return warp


def list_view(request):
    if not hasattr(request,'session'):
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    # 此时一定是已登录
    user_id = request.session['user']['id']
    # 根据已登录的用户id找到当前登录的用户
    user = User.objects.get(id=user_id)
    notes = user.note_set.all()
    return render(request,'note/showall.html',locals())


def list_page_view(request):
    if not hasattr(request,'session'):
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    # 此时一定是已登录
    user_id = request.session['user']['id']
    # 根据已登录的用户id找到当前登录的用户
    user = User.objects.get(id=user_id)
    notes = user.note_set.all()
    # 在此处添加分页功能
    paginator = Paginator(notes,5)
    # 得到当前的页码数
    cur_page = request.GET.get('page',1)
    cur_page = int(cur_page)    # 转为数字
    page = paginator.page(cur_page)
    return render(request,'note/listpage.html',locals())


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request,'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        # 得到当前用户信息
        user_id = request.session['user']['id']
        user = User.objects.get(id=user_id)
        note = models.Note(user=user)
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/')


@check_login
def mod_view(request,id):
    # 得到当前登录用户的模型对象
    user_id = request.session['user']['id']
    user = User.objects.get(id=user_id)
    note = models.Note.objects.get(user=user,id=id)
    if request.method == 'GET':
       return render(request,'note/mod_note.html',locals())
    elif request.method == 'POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/')


@check_login
def del_view(request,id):
    # 得到当前登录用户的模型对象
    user_id = request.session['user']['id']
    user = User.objects.get(id=user_id)
    note = models.Note.objects.get(user=user, id=id)
    note.delete()
    return HttpResponseRedirect('/note/')

