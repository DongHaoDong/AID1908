from django.shortcuts import render

# Create your views here.
# file:index/views.py
from django.http import HttpResponse



def index_view(request):
    return render(request,'index/index.html',locals())


def test_view(request):
    print('test_view被调用')
    return HttpResponse("请求到达了/test页面")


from django.conf import settings
import os

def upload_view(request):
    if request.method == 'GET':
        return render(request,'index/upload.html')
    elif request.method == 'POST':
        files = request.FILES['myfile']
        filename = os.path.join(settings.MEDIA_ROOT,files.name)
        with open(filename,'wb') as fw:
            fw.write(files.file.read())
            return HttpResponse('收到上传文件'+files.name+"成功")
        return HttpResponse("文件上传失败！")

