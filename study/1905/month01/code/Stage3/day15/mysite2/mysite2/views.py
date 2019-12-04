# file: mysite2/views.py

from django.http import HttpResponse


def sum_view(request):
    if request.method == 'GET':
        try:
            start = request.GET.get('start', '0')
            start = int(start)
            stop = request.GET['stop']
            stop = int(stop)
            step = request.GET.get('step', '1')
            step = int(step)
            mysum = sum(range(start, stop, step))
            html = '和是: %d' % mysum
            return HttpResponse(html)
        except Exception as err:
            return HttpResponse("您提供的查询字符串无效!")


login_form_html = '''
<form method="post" action="/login">
    账号:<input type="text" name="username">
    密码:<input type="password" name="password">
    <input type="submit" value="登录">
</form>
'''


def login_view(request):
    if request.method == 'GET':
        return HttpResponse(login_form_html)
    elif request.method == 'POST':
        name = request.POST.get('username', '账号不能为空')
        s = str(dict(request.POST))
        html = '账号:' + name
        html += s
        return HttpResponse(html)


def login2_view(request):
    if request.method == 'GET':
        # 返回模板生成的html给浏览器
        # 方法1
        # # 1. 先加载模块
        # from django.template import loader
        # t = loader.get_template('mylogin.html')
        # # 2. 用模板生成html
        # html = t.render({"username":"dream"})
        # # 3. 将html返回给浏览器
        # return HttpResponse(html)

        # 方法2
        from django.shortcuts import render
        return render(request,"mylogin.html",{"username":'董浩东'})


from django.shortcuts import render


def say_hello():
    return "你好"
class Dog:
    def say(self):
        return "汪汪！"


def test_view(request):
    s = "Hello Dream!"
    lst = ['北京','上海','广东','深圳','西安']
    mydic = {'name':'董浩东','age':20}
    dic = {
        "s":s,
        "lst":lst,
        "mydic":mydic,
        "say_hello":say_hello,
        'dog1':Dog()
    }
    return render(request,'test.html',dic)


def mytemp_view(request):
    # dic = {
    #     "x":10
    # }
    x=-5
    return render(request,'mytemp.html',locals())


def mycalc_view(request):
    if request.method == 'GET':
        return render(request,'mycalc.html')
    elif request.method == 'POST':
        x = int(request.POST.get('x','0'))
        y = int(request.POST.get('y','0'))
        op = request.POST.get('op')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request,'mycalc.html',locals())


def for_view(request):
    lst = ['北京','上海','广东','深圳','西安']
    s = "<i>Hello World</i>"
    n = 100
    s2 = 'aa bb cc dd ee ff'
    return render(request,'for.html',locals())


def index_view(request):
    return render(request,'base.html')


def sport_view(request):
    return render(request,'sport.html')


def news_view(request):
    return render(request,'news.html')

def pagen_view(request,n):
    return HttpResponse("第" + n + "页")