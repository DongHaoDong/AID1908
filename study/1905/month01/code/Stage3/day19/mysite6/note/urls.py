from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.list_view),
    re_path(r'^add',views.add_view),
    re_path(r'^mod/(\d+)',views.mod_view),
    re_path(r'^del/(\d+)',views.del_view),
]