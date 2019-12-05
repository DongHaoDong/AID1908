from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# file:bookstore/views.py

from . import models
def add_view(request):
    try:
        # 方法1
        # abook = models.Book.objects.create(title='C++',price=68)

        # 方法2
        abook = models.Book(price=98)
        abook.title = 'Python'
        abook.save()    # 真正指定SQL语句
        return HttpResponse("添加图书成功！")
    except Exception as err:
        return HttpResponse("添加图书失败!")
