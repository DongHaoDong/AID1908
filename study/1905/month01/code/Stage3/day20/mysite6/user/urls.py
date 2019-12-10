from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^reg$',views.reg_view),
    re_path(r'^login',views.login_view),
    re_path(r'^logout',views.logout_view),
    re_path(r'^register$',views.register_view),
]