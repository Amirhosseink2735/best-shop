from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from .shop_cart import shopcart
from apps.products.models import Product

#----------------------------------------------------------------
#کلاس برای نمایش سبد خرید 
class Show_Shopcart(View):
    def get(self,request):
        shop_cart=shopcart(request)
        total_price=shop_cart.clc_total_price()
        print(total_price)
        
        
        context={
            "shop_carts":shop_cart,
            
        }
        
        
        return render(request,"orders/show_shopcart.html",context)







#----------------------------------------------------------------
#اضافه کردن به سبد خرید 
def add_to_shopcart(request):
    shop_cart=shopcart(request)
    product_id=request.GET.get("product_id")
    product=get_object_or_404(Product,id=product_id)
    qty=request.GET.get("qty")
    shop_cart.add_to_shop_cart(product,qty)
    return HttpResponse("محصول به سبد خرید اضافه شد !!!")
    

#----------------------------------------------------------------








