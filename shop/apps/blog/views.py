from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.db.models import Q
from django.views import View

#-----------------------------------------------------

#برای خواندنی ها
def Readable(request):
    blogs=Blog.objects.filter(Q(is_active=True)).order_by("-register_date")[:8]
    return render(request,"blog/readable.html",{"blogs":blogs})


#-----------------------------------------------------
#جزعبات بلاگ

class BlogDetails(View):
    def get(self,request,slug):
        blog=get_object_or_404(Blog,slug=slug)
        
        
        return render(request,"blog/blog_datails.html",{"blog":blog})
    

#-----------------------------------------------------
#مقالات مرتبط
def related_blogs(request,slug):
    pass

    





