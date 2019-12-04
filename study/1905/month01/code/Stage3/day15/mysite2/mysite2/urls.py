"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from .views import sum_view
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'sum',sum_view),
    re_path(r'^login$',views.login_view),
    re_path(r'^login2$',views.login2_view),
    re_path(r'^test$',views.test_view),
    re_path(r'^test2$',views.mytemp_view),
    re_path(r'^mycalc$',views.mycalc_view),
    re_path(r'^test_for',views.for_view),
    re_path(r'^$',views.index_view),
    re_path(r'^sport',views.sport_view,name='sport'),
    re_path(r'^news',views.news_view,name='news'),
    re_path(r'^page(\d+)',views.pagen_view,name='pagen')
]
