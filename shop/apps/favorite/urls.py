from django.contrib import admin
from django.urls import path
import apps.favorite.views as vv
app_name="fav"

urlpatterns = [
    path("user_favorite/",vv.user_favorite,name="user_favorite"),
    path("show_sliders/",vv.show_sliders,name="show_sliders"),

]
