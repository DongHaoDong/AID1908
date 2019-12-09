from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class MyMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print("中间件方法process_request被调用")
        print("路由是:",request.path)
        print("请求方式是:",request.method)
        if request.path=='/aaa':
            return HttpResponse("当前路由是:/aaa")


from django.http import HttpResponse
from django.http import Http404


class VisitLimit(MiddlewareMixin):
    # 次字典的键为IP地址，值为此地址的访问次数
    visit_times = {}

    def process_request(self,request):
        ip = request.META['REMOTE_ADDR'] # 得到客户端IP
        if request.path_info != '/test':
            return None
        # 获取以前的访问次数
        times = self.visit_times.get(ip,0)
        print("IP",ip,'已访问过/test',times,"次")
        self.visit_times[ip] = times + 1
        if times < 5:
            return None
        return HttpResponse("您已经访问过:"+str(times)+"次")