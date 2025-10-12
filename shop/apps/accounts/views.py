from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from .models import Customuser
from utils import create_random_code
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


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





