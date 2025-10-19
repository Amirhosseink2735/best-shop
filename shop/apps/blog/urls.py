from django.contrib import admin
from django.urls import path
import apps.blog.views as vv
app_name="blog"

urlpatterns = [
    path("readable/",vv.Readable,name="readable"),

]
