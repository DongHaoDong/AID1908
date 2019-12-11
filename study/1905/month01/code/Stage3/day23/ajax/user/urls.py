from django.urls import path
from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^xhr/$',views.xhr,name='xhr'),
    re_path(r'^get-xhr/$', views.get_xhr,name='get-xhr'),
    re_path(r'^get-xhr-server/$', views.get_xhr_server,name='get-xhr-server'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^checkname/$',views.checkname,name='checkname'),
    re_path(r'^make_post/$',views.make_post,name='make_post'),
    re_path(r'^get_user/$',views.get_user,name='get_user'),
    re_path(r'^get_user_server/$',views.get_user_server,name='get_user_server'),
    re_path(r'^json_object/$',views.json_object,name='json_object'),
    re_path(r'^json_dumps/$',views.json_dumps,name='json_dumps'),
]