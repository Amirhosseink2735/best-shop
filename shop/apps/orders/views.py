from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.db.models import Q
from .shop_cart import shopcart
from apps.products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order,OrderDetails,City,State
from apps.accounts.models import Customer


#----------------------------------------------------------------
#کلاس برای نمایش سبد خرید 
class Show_Shopcart(View):
    def get(self,request):
        shop_cart=shopcart(request)

        
        return render(request,"orders/show_shopcart.html")


#----------------------------------------------------------------

def show_shop_cart_tabel(request):
    shop_cart=shopcart(request)
    shop_cart=shopcart(request)
    clc_total_price=shop_cart.clc_total_price()
    tax=0.009*clc_total_price
    dlivery=70000
    if clc_total_price>500000:
        dlivery=0
    t_price=tax+dlivery+clc_total_price
  
        
    context={
            "shop_carts":shop_cart,
            "clc_total_price":clc_total_price,
            "tax":tax,
            "dlivery":dlivery,
            "t_price":t_price,
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
from django.contrib.auth.mixins import LoginRequiredMixin
class CheckOut(LoginRequiredMixin,View):
    def get(self,request):
        user=request.user
        shop_cart=shopcart(request)
        try:
            customer=get_object_or_404(Customer,user=user)


        except:
            customer=Customer.objects.create(
                user=user,
                phone_number=user.mobile_number
            )
        order=Order.objects.create(
            customer=customer,
        )
        for item in shop_cart:
            OrderDetails.objects.create(
                order=order,
                product=item["product"],
                qty=item["qty"],
                price=item["price"]
            )
        clc_total_price=shop_cart.clc_total_price()
        tax=0.09*clc_total_price
        dlivery=70000
        if clc_total_price>500000:
            dlivery=0

        t_price=tax+dlivery+clc_total_price
    
        citys=City.objects.filter(Q(is_active=True))
        
        
        context={
            "shop_carts":shop_cart,
            "clc_total_price":clc_total_price,
            "tax":tax,
            "dlivery":dlivery,
            "t_price":t_price,
            "citys":citys,
        }

        

        
        return render(request,"orders/checkout.html",context)


#-----------------------------------------------------------------------------












