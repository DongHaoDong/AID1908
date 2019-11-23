# file: mysite1/views.py

from django.http import HttpResponse


def page1_view(request):
    html = "<h1>这是第1个页面</h1>"
    return HttpResponse(html)