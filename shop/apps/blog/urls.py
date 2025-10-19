from django.contrib import admin
from django.urls import path
import apps.blog.views as vv
app_name="blog"

urlpatterns = [
    path("readable/",vv.Readable,name="readable"),
    path("blog_details/<slug:slug>",vv.BlogDetails.as_view(),name="blog_details"),
    path("related_blogs/<slug:slug>",vv.related_blogs,name="related_blogs"),
    path("show_blogs/",vv.Show_blogs.as_view(),name="show_blogs"),

]
