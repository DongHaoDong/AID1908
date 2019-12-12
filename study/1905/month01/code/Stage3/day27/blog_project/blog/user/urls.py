from django.urls import re_path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/v1/users
    re_path(r'^$',views.users),
]