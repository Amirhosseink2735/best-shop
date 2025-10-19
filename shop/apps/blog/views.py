from django.shortcuts import render
from .models import Blog
from django.db.models import Q

#-----------------------------------------------------
#برای خواندنی ها
def Readable(request):
    blogs=Blog.objects.filter(Q(is_active=True)).order_by("-register_date")[:8]
    return render(request,"blog/readable.html",{"blogs":blogs})





