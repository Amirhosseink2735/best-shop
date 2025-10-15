from django.shortcuts import render,get_object_or_404,redirect
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

        
        return render(request,"orders/show_shopcart.html")


#----------------------------------------------------------------

def show_shop_cart_tabel(request):
    shop_cart=shopcart(request)
    clc_total_price=shop_cart.clc_total_price()
    tax=0.09*clc_total_price
    dlivery=70000
    if clc_total_price>500000:
        dlivery=0
  
        
    context={
            "shop_carts":shop_cart,
            "clc_total_price":clc_total_price,
            "tax":tax,
            "dlivery":dlivery
        }

    return render(request,"orders/shop_cart_tabel.html",context)








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
#برای حذف عنصر از سبد خرید

def delete_from_shopcart(request):
    product_id=request.GET.get("product_id")
    product=get_object_or_404(Product,id=product_id)
    shop_cart=shopcart(request)
    shop_cart.delete_from_shop_cart(product)

    return redirect("ord:show_shop_cart_tabel")


#-------------------------------------------------------------




