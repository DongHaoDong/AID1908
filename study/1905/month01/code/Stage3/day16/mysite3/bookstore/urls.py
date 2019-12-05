# file: bookstore/urls.py

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^add_book',views.add_view),
]