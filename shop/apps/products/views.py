from django.shortcuts import render,get_object_or_404
from django.views import View
from django.db.models import Q
from .models import Product,ProductGroup,ProductGallery,ProductFeature

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


#--------------------------------------------------------
#جزعیات محصول
class ProductDetails(View):
    def get(self,request,slug):
        product=get_object_or_404(Product,slug=slug)
        product_gallerys=ProductGallery.objects.filter(Q(product=product))
        features=ProductFeature.objects.filter(product=product)
        

        
        context={
            "product":product,
            "images":product_gallerys,
            "features":features,
        }        
        return render(request,"products/productdetails.html",context)







