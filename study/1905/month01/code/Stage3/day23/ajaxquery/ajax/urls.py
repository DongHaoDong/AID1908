from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^load_test/$',views.load_test),
    re_path(r'^load_test_server',views.load_test_server),
]