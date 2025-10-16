from django.contrib import admin
from .models import City,State

#----------------------------------------------------------------

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=("city_name","is_active")
    list_filter=("city_name",)
    list_editable=("is_active",)
    

#----------------------------------------------------------------
@admin.register(State)

class StateAdmin(admin.ModelAdmin):
    list_display=("state_name","is_active")
    list_filter=("state_name",)
    list_editable=("is_active",)
    
    
#----------------------------------------------------------------    


