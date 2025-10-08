from django.contrib import admin
from .forms import UsercreationForm,UserChangeForm
from .models import Customuser
from django.contrib.auth.admin import UserAdmin


@admin.register(Customuser)
class CreationUserAdmin(UserAdmin):
    form=UserChangeForm
    add_form=UsercreationForm
    list_display=("mobile_number","email","name","family","gender","is_active","is_admin")
    list_filter=("is_active","is_admin","family")
    
    
    fieldsets = (
        (None,{'fields':("mobile_number","password")}),
        ("personal info",{'fields':("email","name","family","gender","active_code")}),
        ("permissions",{"fields":("is_active","is_admin","is_superuser","groups","user_permissions")}),
    )
    
    
    
    add_fieldsets=(
        (None,{"fields":("mobile_number","email","name","family","gender","password1","password2")}),
        
    )
    
    search_fields=("mobile_number",)
    list_editable=["is_active","is_admin"]
    ordering=("mobile_number",)
    
    
    filter_horizontal=("groups",'user_permissions')
    
    
    


