from django.shortcuts import render

# Create your views here.


def load_test(request):
    return render(request,'load_test.html')


def load_test_server(request):
    return render(request,'load_test_server.html')
