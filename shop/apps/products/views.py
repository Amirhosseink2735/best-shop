from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import Product,ProductGroup

#---------------------------------------------------

#ارزان ترین محصولات 

def cheapest_products(request):
    products=Product.objects.filter(Q(is_active=True)).order_by("price")[:6]
    return render(request,"products/cheapest_products.html",{"products":products})

#------------------------------------------------------

#جدیدترین محصولات 

def get_product_group(request):
    product_groups=ProductGroup.objects.filter(Q(is_active=True)).order_by("-register_date")[:7]
    return render(request,"products/get_product_group.html",{"product_groups":product_groups})


