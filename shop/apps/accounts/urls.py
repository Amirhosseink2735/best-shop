from django.contrib import admin
from django.urls import path
import apps.accounts.views as vv
app_name="accounts"

urlpatterns = [
    path("mobile_number1/",vv.mobile_number1,name="mobile_number1"),
    path("get_active_code/",vv.get_active_code,name="get_active_code"),
    path("logout_user/",vv.logout_user,name="logout_user"),
    path("main_user_panel/",vv.MainUserPanel.as_view(),name="main_user_panel"),
    path("show_main_panel/",vv.show_main_panel,name="show_main_panel"),
    path("show_favorite/",vv.show_favorite,name="show_favorite"),
    path("personal_details/",vv.Personal_Details.as_view(),name="personal_details"),
    path("save_data/",vv.save_personal_data,name="save_data"),
]
