# file: mysite1/views.py

from django.http import HttpResponse
from django.http import HttpResponseRedirect

index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="/mypage?a=888&b=999">进入mypage</a>
<form action="/mypage" method="get">
    <input type="text" name="a"><br/>
    <input type="text" name="b">
    <input type="submit" value="提交">
</form>
</body>
</html>
'''

def index_view(request):
    # html = "<h1>这是我的首页</h1>"
    return HttpResponse(index_html)


def page1_view(request):
    html = "<h1>这这是编号为1的网页</h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是编号为2的网页</h1>"
    return HttpResponse(html)


def pagen_view(request, n):
    html = "<h1>=============这是编号为%s的网页=============</h1>"%n
    return HttpResponse(html)


def math_view(request, x, op, y):
    x = int(x)  # 转为整数
    y = int(y)  # 转为整数
    result = None
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y
    if result is None:
        # return HttpResponse("出错啦！！！")
        return HttpResponseRedirect("https://www.baidu.com")
    html = "结果:"+str(result)
    html += "您的IP是:"+request.META['REMOTE_ADDR']
    print(html)
    return HttpResponse(html)


def person_view(request,name=None,age=None):
    s = "姓名:" + name
    s += "年龄:" + age
    return HttpResponse(s)

# def person_view(request,**kwargs):
#     s = str(kwargs)
#     return HttpResponse(s)


def birthday_view(request, y, m, d):
    html = "生日:" + y + "年" + m + "月" + d + "日"
    return HttpResponse(html)


# def birthday_view2(request, m, d, y):
#     html = "生日:" + y + "年" + m + "月" + d + "日"
#     return HttpResponse(html)


def mypage_view(request):
    '''
    此函数用来表示已得到GET请求中的查询参数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        # a = request.GET['a']
        # a = request.GET.get('a','没有对应的值')
        a = request.GET.getlist('a')    # ['100']
        html = "a = " + str(a)
        b = request.GET.getlist('b')  # ['200','400']
        html += "b = " + str(b)
        # html = str(dict(request.GET))
        return HttpResponse(html)
    else:
        return HttpResponse('当前不是GET请求')