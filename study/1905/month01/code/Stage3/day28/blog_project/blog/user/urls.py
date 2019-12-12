from django.urls import re_path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/v1/users
    re_path(r'^$',views.users),
    # http://127.0.0.1:8000/v1/users/<username>
    # APPEND_SLASH自动补全url后面的斜线，前提是你有一个带/的路由
    re_path(r'^/(?P<username>[\w]{1,11})$',views.users),
    # http://127.0.0.1:8000/v1/users/<username>/avatar
    re_path(r'^/(?P<username>[\w]{1,11})/avatar$',views.user_avatar),
]