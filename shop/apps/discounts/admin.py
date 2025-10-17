from django.contrib import admin
from .models import DiscountBasket,DiscountBasketDetails


    
    
class DiscountBasketDetailsAdmin(admin.TabularInline):
    model=DiscountBasketDetails
    extra=3
    
    



@admin.register(DiscountBasket)
class DiscountBasketAdmin(admin.ModelAdmin):
    list_display=("discount_title","start_date","end_date","discount","is_active")
    ordering=("is_active",)
    inlines=[DiscountBasketDetailsAdmin]

