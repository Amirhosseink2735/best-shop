from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from .models import Customuser
from utils import create_random_code


#------------------------------------------------------
#کلاس برای گرفتن شماره موبایل 

def mobile_number1(request):
    mobile_number=request.GET.get("mobile_number")
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

#تابع برای گرفتن کد فعالسازی و چک کردن ان 
def get_active_code(request):
    active_code=request.GET.get("code")
    print(active_code)
    return HttpResponse("ok")








