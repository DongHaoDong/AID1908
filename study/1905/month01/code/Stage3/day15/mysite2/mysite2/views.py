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

