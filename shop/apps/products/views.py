from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.db.models import Q,Count
from .models import Product,ProductGroup,ProductGallery,ProductFeature,Brand

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

#-----------------------------------------------------------
#برای مشاهده همه محصولات ارزان 

class Show_AllProduct(View):
    def get(self,request,*args, **kwargs):
        products=Product.objects.filter(Q(is_active=True)).order_by('price')
        l1=[]
        for item in products:
            l1.append(item.price)
        min_price=min(l1)
        max_price=max(l1)
        
        
        brand_listid=request.GET.getlist("brands")
        
        if brand_listid:
            products=products.filter(Q(brand__id__in=brand_listid))
            
        mojod=request.GET.get("mojod")
        #بعد بخش انبار داری درستش کن 
        
    
        context={
            "products":products,
            "min_price":min_price,
            "max_price":max_price,
            
        }
        
        
        return render(request,"products/all_products.html",context)


#-----------------------------------------------------------
#برای محصولات یه گروه خاص

class Show_products_in_groups(View):
    def get(self,request,slug):
        product_group=get_object_or_404(ProductGroup,slug=slug)
        products=Product.objects.filter(Q(is_active=True) & Q(product_group=product_group)).order_by("price")[:10]


        context={
            "product_group":product_group,
            "products":products
        }
                
        return render(request,"products/show_products_in_groups.html",context)
    
    
    
    
    
#----------------------------------------------------------------------------------

#تابع برای محصولات جدید 

def new_products1(request):
    products=Product.objects.filter(Q(is_active=True)).order_by("-register_date")[:10]
    return render(request,"products/new_products1.html",{"products":products})
        
    
#----------------------------------------------------------------------------------

#تابع برای محصولات جدید 

def new_products2(request):
    products=Product.objects.filter(Q(is_active=True)).order_by("-register_date")[:10]
    return render(request,"products/new_products2.html",{"products":products})
        
    
#----------------------------------------------------------------------------------
    
#کلاس مشاهده همه محصولات بر اساس جدید بودن 

class Show_all_newproducts(View):
    def get(self,request):
        products=Product.objects.filter(Q(is_active=True)).order_by("-register_date")[:10]    
        return render(request,"products/show_all_newproducts.html",{"products":products})
    
#-----------------------------------------------------------------------------------

#برای برندها
def get_brands(request):
    brands=Brand.objects.filter(Q(is_active=True))
    return render(request,"products/get_brands.html",{"brands":brands})    
    
    
#------------------------------------------------------------------------------------

#دسته بندی ها برای فیلتر 

def product_group_for_filter(request):
    product_groups=ProductGroup.objects.filter(Q(is_active=True))\
        .annotate(count=Count("products_of_group")).order_by("-count")[:6]
    return render(request,"products/product_group_for_filter.html",{"product_groups":product_groups})



#--------------------------------------------------------------------------------------

#برندها برای فیلتر کردن 
def brands_for_filter(request):
    brands=Brand.objects.filter(Q(is_active=True)).annotate(count=Count("product_of_brands"))\
        .order_by("-count")[:6]

    return render(request,"products/brands_for_filter.html",{"brands":brands})

#---------------------------------------------------------------------------------------
 
#برای محصولات مرتبط

def releated_products(request,slug):
    product=get_object_or_404(Product,slug=slug)
    
    product_groups=product.product_group.all()
    
    r_products=Product.objects.filter(Q(is_active=True)&Q(product_group__in=product_groups)).exclude(id=product.id).distinct()[:15]
    
    return render(request,"products/related_product.html",{"r_products":r_products})





 
 
 




#---------------------------------------------------------------------------------------