from django.shortcuts import render
from apps.products.models import Product
from django.db.models import Q
#-------------------------------------------------------------


def search_products(request):
    q=request.GET.get("q")
    products=Product.objects.filter(
        Q(is_active=True)&Q(product_name__icontains=q)|Q(description__icontains=q)
    )
            
    return render(request,"search_app/search_results.html",{"products":products})




