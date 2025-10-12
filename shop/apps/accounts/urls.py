from django.contrib import admin
from django.urls import path
import apps.accounts.views as vv
app_name="accounts"

urlpatterns = [
    path("mobile_number1/",vv.mobile_number1,name="mobile_number1"),
    path("get_active_code/",vv.get_active_code,name="get_active_code"),
    path("logout_user/",vv.logout_user,name="logout_user"),

    
    
]
