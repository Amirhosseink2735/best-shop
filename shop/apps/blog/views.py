from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogGroup
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
    blog=Blog.objects.get(slug=slug)
    blog_groups=blog.blog_group.all()
    r_blogs=Blog.objects.filter(Q(is_active=True)&Q(blog_group__in=blog_groups)).exclude(id=blog.id).distinct()[:3]
    return render(request,"blog/related_blogs.html",{"r_blogs":r_blogs})

#-----------------------------------------------------

#نمایش تمای مقالات 
class Show_blogs(View):
    def get(self,request):
        blogs=Blog.objects.filter(Q(is_active=True)).order_by("-published_date")[:5]
        return render(request,"blog/show_blogs.html",{"blogs":blogs})








