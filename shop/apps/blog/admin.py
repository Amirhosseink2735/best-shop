from django.contrib import admin
from .models import Blog,BlogGroup

#----------------------------------------------------------
def active_products(modeladmin,request,queryset):
    res=queryset.update(is_active=True)
    message=f"تعداد{res}فعال شد."
    modeladmin.message_user(request,message)
    
def de_active_products(modeladmin,request,queryset):
    res=queryset.update(is_active=False)
    message=f"تعداد{res}مقاله غیر فعال شد "
    modeladmin.message_user(request,message)

@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display=("blog_name","blog_name","blog_title","is_active","register_date")
    list_filter=("is_active",)
    list_editable=("is_active",)
    ordering=("is_active","register_date")
    actions=[active_products,de_active_products]
    
#----------------------------------------------------------
@admin.register(BlogGroup)
class BlogGroupAdmin(admin.ModelAdmin):
    list_display=("group_name","is_active")
    list_editable=("is_active",)
    list_editable=("is_active",)
    
    
#----------------------------------------------------------