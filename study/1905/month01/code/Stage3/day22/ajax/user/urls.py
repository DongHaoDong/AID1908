from django.urls import path
from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^xhr/$',views.xhr,name='xhr'),
    re_path(r'^get-xhr/$', views.get_xhr,name='get-xhr'),
    re_path(r'^get-xhr-server/$', views.get_xhr_server,name='get-xhr-server'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^checkname/$',views.checkname,name='checkname'),
    re_path(r'^make_post/',views.make_post,name='make_post')
]