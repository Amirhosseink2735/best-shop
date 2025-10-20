from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from .models import Customuser,Customer
from utils import create_random_code
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from apps.orders.models import Order,OrderDetails
from apps.favorite.models import Favorite
from .forms import PersonalDetailsForm

#------------------------------------------------------
#کلاس برای گرفتن شماره موبایل 

def mobile_number1(request):
    mobile_number=request.GET.get("mobile_number")
    request.session["user_session"]={
        "mobile_number":mobile_number,
    }
    try:
        user=Customuser.objects.get(mobile_number=mobile_number)
        
    except:
        user=Customuser.objects. create_user(
            mobile_number=mobile_number,
            active_code=create_random_code(6),
 
        )
        user.save()
    return HttpResponse("لطفا کد فعالسازی را وارد کنید ")



#------------------------------------------------------------------
#تابع گرفتن کد فعالسازی و مقایسه ان 

def get_active_code(request):
    active_code=request.POST.get("activecode")
    user_session=request.session["user_session"]
    mobile_number=user_session["mobile_number"]
    user=get_object_or_404(Customuser,mobile_number=mobile_number)
    if user.active_code==active_code:
        login(request,user)
        user.active_code=create_random_code(6)
        user.save()
        next_url=request.GET.get("next")
        if next_url:
            messages.success(request,"با موفقیت وارد شدید","success")
            return redirect("main:index")
        else:
            messages.success(request,"با موفقیت وارد شدید","success")
            return redirect("main:index")
    else:
        messages.error(request,"کد فعالسازی درست نمی باشد","danger")
        return redirect("main:index")
            
    
#---------------------------------------------------------------------
#تابع خروج 

def logout_user(request):
    logout(request)
    messages.error(request,"خارج شدید","error")
    return redirect("main:index")

#---------------------------------------------------------------------
#نمایش پنل کاریری
class MainUserPanel(View):
    def get(self,request):
        
        return render(request,"user_panel.html")


#---------------------------------------------------------------------
def show_main_panel(request):
    user=request.user
    count_orders=0
    try:   
        user=request.user
        customer=Customer.objects.get(user=user)
        orders=Order.objects.filter(Q(customer=customer)&Q(is_finaly=True))[:8]
        count_orders=Order.objects.filter(Q(customer=customer)&Q(is_finaly=True)).count()
        
        
    except:
        count_orders=0

    context={
        "count_orders":count_orders,
        "orders":orders,
    }
    return render(request,"accounts/main_user_panel.html",context)

#---------------------------------------------------------------------
#برای علاقه مندی ها در پنل کاربری 
def show_favorite(request):
    user=request.user
    fav_products=Favorite.objects.filter(Q(favorite_user=user))[:6]
    return render(request,"accounts/show_favorite.html",{"fav_products":fav_products})
           
#---------------------------------------------------------------------
#برای نمایش اطلاعات کاربر در گنل کاربری 
class Personal_Details(View):
    def get(self,request):
        user=request.user
        initial_dict={
            "name":user.name,
            "family":user.family,
            "mobile_number":user.mobile_number,
            "email":user.email
        }
        form=PersonalDetailsForm(initial=initial_dict)
        
        return render(request,"accounts/personal_details.html",{"form":form})
    

#---------------------------------------------------------------------
#گرفتن اطلاعات و ذخیره 
def save_personal_data(request):
    form=PersonalDetailsForm(request.POST)
    gender1=request.POST.get("gender")
    print(gender1)
    user=request.user
    if form.is_valid():
        cd=form.cleaned_data
        try:
            customer=Customer.objects.get(user=user)
            customer.phone_number=cd["mobile_number"]
            customer.save()
            if gender1=="1":
                user.gender=True
            else:
                user.gender=False
            user.mobile_number=cd["mobile_number"]
            user.name=cd["name"]
            user.family=cd["family"]
            user.email=cd["email"]
            user.save()
        except:
            if gender1=="1":
                user.gender=True
            else:
                user.gender=False
            user.mobile_number=cd["mobile_number"]
            user.name=cd["name"]
            user.family=cd["family"]
            user.email=cd["email"]
            user.save()           
    
    
    return redirect("main:index")
           
    
#--------------------------------------------------------------------------------
#برای حذف از علاقه مندی ها در پنل کاربری 
from apps.products.models import Product
def delete_favorite_user_panel(request,slug):
    product=get_object_or_404(Product,slug=slug)
    Favorite.objects.get(Q(favorite_user=request.user)&Q(product=product)).delete()
    return redirect("accounts:show_favorite")
    

    
    
    
    
    
    
