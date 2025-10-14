from django.contrib import admin
from django.urls import path
import apps.orders.views as vv
app_name="ord"

urlpatterns = [
    path("add_shopcart/",vv.add_to_shopcart,name="add_shopcart"),
    path("show_shopcart/",vv.Show_Shopcart.as_view(),name="show_shopcart"),
    
]
