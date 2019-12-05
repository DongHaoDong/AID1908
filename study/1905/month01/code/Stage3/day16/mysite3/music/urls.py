# file : music/urls.py

from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^page1',views.page1_view),
    re_path(r'^page2',views.page2_view),
    re_path(r'^page3',views.page3_view),
    re_path(r'^index',views.index_view)
]

