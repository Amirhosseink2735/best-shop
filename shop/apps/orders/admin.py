from django.contrib import admin
from .models import State


#----------------------------------------------------------------
@admin.register(State)

class StateAdmin(admin.ModelAdmin):
    list_display=("state_name","is_active")
    list_filter=("state_name",)
    list_editable=("is_active",)
    
    
#----------------------------------------------------------------    


