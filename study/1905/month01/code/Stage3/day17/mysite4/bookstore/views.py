from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

# file:bookstore/views.py

from . import models


def add_view(request):
    if request.method == 'GET':
        return render(request,'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        try:
            models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=market_price,
            )
            # return HttpResponse("添加成功！")
            return HttpResponseRedirect('/bookstore/all')
        except:
            return HttpResponse("添加失败！")


def show_all(request):
    books = models.Book.objects.all()
    # books = models.Book.objects.filter(price__lt=50)
    # books = models.Book.objects.filter(price__range=(50,80))
    # books = models.Book.objects.exclude(pub__contains='清华大学')
    # books = models.Book.objects.exclude(pub__contains='清华大学',market_price__lt=40)
    # for book in books:
    #     print("书名:"+book.title)
    # return HttpResponse('查询成功！')
    return render(request,'bookstore/list.html',locals())


def mod_view(request,id):
    try:
        book = models.Book.objects.get(id=id)
    except:
        return HttpResponse("没有id为"+id+"的数据记录")
    if request.method == 'GET':
        return render(request,'bookstore/mod.html',locals())
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price','0'))
        market_price = float(request.POST.get('market_price','0'))
        book.title = title
        book.pub = pub
        book.price = price
        book.market_price = market_price
        book.save()
        return HttpResponseRedirect('/bookstore/all')
        # return HttpResponseRedirect('../all')


def del_view(request,id):
    try:
        book = models.Book.objects.get(id=id)
    except Exception as err:
        return HttpResponse("删除失败")
    book.delete()
    return HttpResponseRedirect('/bookstore/all')