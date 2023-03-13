from django.urls import re_path
from rep_app import views

urlpatterns = [
    re_path(r'^company$', views.company_api),
    re_path(r'^company/([0-9]+)$', views.company_api),

    re_path(r'^user$', views.user_api),
    re_path(r'^user/([0-9]+)$', views.user_api),

    re_path(r'^device$', views.device_api),
    re_path(r'^device/([0-9]+)$', views.device_api),

]