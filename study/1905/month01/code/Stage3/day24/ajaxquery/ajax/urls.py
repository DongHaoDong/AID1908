from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^load_test/$',views.load_test),
    re_path(r'^load_test_server/$',views.load_test_server),
    re_path(r'^jquery_get/$',views.jquery_get),
    re_path(r'^jquery_get_server/$',views.jquery_get_server),
    re_path(r'^jquery_post/$',views.jquery_post),
    re_path(r'^jquery_post_server/$',views.jquery_post_server),
    re_path(r'^jquery_ajax/$',views.jquery_ajax),
    re_path(r'^jquery_ajax_server/$',views.jquery_ajax_server),
    re_path(r'^jquery_ajax_user/$',views.jquery_ajax_user),
    re_path(r'^jquery_ajax_user_server/$',views.jquery_ajax_user_server),
    re_path(r'^cross/$',views.cross),
    re_path(r'^cross_server/$',views.cross_server),
    re_path(r'^cross_server_json/$',views.cross_server_json),
]