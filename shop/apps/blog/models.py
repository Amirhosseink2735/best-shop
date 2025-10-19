from django.db import models
from utils import FileUpload
from apps.accounts.models import Customuser
from apps.products.models import Product


#------------------------------------------------------------------------------

class Blog(models.Model):
    blog_name=models.CharField(verbose_name="نام مقاله",max_length=100)
    author=models.ForeignKey(Customuser,verbose_name="نویسنده مقاله",on_delete=models.CASCADE,related_name="author_blog")
    file_upload=FileUpload("blog","brand")
    image_name=models.ImageField(upload_to=file_upload.upload_to,verbose_name="تصویر مقاله")
    is_active=models.BooleanField(default=False,verbose_name="وضعیت فعال/غیرفعال")
    blog_text=models.TextField(verbose_name="متن مقاله")
    description=models.TextField(verbose_name="توضیحات",null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="blog_product",null=True,blank=True)
    register_date=models.DateTimeField(auto_now_add=True,verbose_name="زمان درج")
    published_date=models.DateTimeField(auto_now=True,verbose_name="تاریخ انتشار")
    
    
    def __str__(self):
        return f"{self.blog_name} - {self.product}"
    
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
    





