from django import forms
from .models import Customuser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import ModelForm



#--------------------------------------------------------------

class UsercreationForm(forms.ModelForm):
    password1=forms.CharField(label="رمزعبور",widget=forms.PasswordInput(),error_messages={"required":"این فیلد نمیتواند خالی باشد "})
    password2=forms.CharField(label="تکرار رمزعبور",widget=forms.PasswordInput(),error_messages={"required":"این فیلد نمیتواند خالی باشد "})


    class Meta:
        model=Customuser
        fields=["mobile_number","name","family","is_active","email","is_admin","is_superuser"]
        
    def clean_password1(self):
        pass1=self.cleaned_data["password1"]
        pass2=self.cleaned_data["password2"]
        if pass1 and pass2 and pass1!=pass2:
            raise ValidationError("رمز عبور و تکرار ان یکی نمیباشد ")
        
        return pass1
    
    

    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user
    
#----------------------------------------------------------------
    
    
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=Customuser
        fields=["mobile_number","is_active","password","name","family","email","is_admin","is_superuser"]

#----------------------------------------------------------------

class PersonalDetailsForm(forms.Form):
    name=forms.CharField(label="",widget=forms.TextInput(attrs={"class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                                                                "placeholder":"نام","type":"text"}))

    family=forms.CharField(label="",widget=forms.TextInput(attrs={"class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                                                                "placeholder":"نام خانوادگی","type":"text"}))
    
    mobile_number=forms.CharField(label="",widget=forms.TextInput(attrs={"class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                                                                "placeholder":"شماره موبایل  ","type":"text"}))


    email=forms.CharField(label="",widget=forms.TextInput(attrs={"class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                                                                "placeholder":" ایمیل","type":"text"}))


      
        
