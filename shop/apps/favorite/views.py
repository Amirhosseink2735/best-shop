from django.shortcuts import render,get_object_or_404
from .models import Favorite
from apps.products.models import Product
from django.http import HttpResponse
from django.db.models import Q
#---------------------------------------------------------
#برای ثبت علاقه مندی

def user_favorite(request):
    user=request.user
    product_id=request.GET.get("product_id")
    product=get_object_or_404(Product,id=product_id)
    status=Favorite.objects.filter(Q(favorite_user_id=user.id)&Q(product_id=product_id)).exists()
    if status==False:
        Favorite.objects.create(
            product=product,
            favorite_user=user,
            
        )
        return HttpResponse("با موفقیت به لیست علاقه مندی ها اضافه شد !")
    else:
        Favorite.objects.get(Q(product_id=product_id)).delete()
        return HttpResponse("از لیست علاقه مندی ها حذف شد ")
    

    














