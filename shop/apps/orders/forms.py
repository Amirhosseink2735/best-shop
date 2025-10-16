from django import forms


class CheckOutForm(forms.Form):
    
    name=forms.CharField(label="",widget=forms.TextInput(attrs={
        "class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
        "placeholder":"نام","type":"text"
    }))

    family=forms.CharField(label="",widget=forms.TextInput(attrs={
        "class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
        "placeholder":"نام خانوادگی","type":"text"
    }))


    
    address=forms.CharField(label="",widget=forms.TextInput(attrs={
        "class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
        "placeholder":"آدرس","type":"text"
    }))    

    mobile_number=forms.CharField(label="",widget=forms.TextInput(attrs={
        "class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
        "placeholder":"شماره موبایل","type":"text"
    }))
    
    codeposti=forms.CharField(label="",widget=forms.TextInput(attrs={
        "class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
        "placeholder":"کدپستی","type":"text"
    }))
    
    description=forms.CharField(label="",widget=forms.Textarea(attrs={
        "class":"rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
        "placeholder":"توضیحات","type":"text","cols":"30","rows":"7"
    }))    
    
    
    

