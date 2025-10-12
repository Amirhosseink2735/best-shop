from django.contrib import admin
from django.urls import path
import apps.products.views as vv
app_name="products"

urlpatterns = [
    path("cheapest/",vv.cheapest_products,name="cheapest"),
    path("product_groups/",vv.get_product_group,name="product_groups"),

    
    
]
