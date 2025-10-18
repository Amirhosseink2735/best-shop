from django.contrib import admin
from django.urls import path
import apps.search.views as vv
app_name="search"

urlpatterns = [
    path("results/",vv.search_products,name="results"),

    ]
