from django.contrib import admin
from django.urls import path
import apps.products.views as vv
app_name="products"

urlpatterns = [
    path("cheapest/",vv.cheapest_products,name="cheapest"),
    path("product_groups/",vv.get_product_group,name="product_groups"),
    path("product_details/<slug:slug>",vv.ProductDetails.as_view(),name="product_details"),
    path("all_products/",vv.Show_AllProduct.as_view(),name="all_products"),
    path("show_products_in_groups/<slug:slug>",vv.Show_products_in_groups.as_view(),name="show_products_in_groups"),
    
    
]
