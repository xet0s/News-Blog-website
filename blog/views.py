from django.shortcuts import render, get_object_or_404
from .models import Content,Tag

# Create your views here.

def content_list(request): #Bütün içerikleri çeken fonksiyon

    content= Content.objects.filter(admin_approve=True)
    return render(request,"blog/content_list.html", {"contents":content})

def content_detail(request, content_id): #İçerik detaylarını çeken fonksiyon
    content= get_object_or_404(Content, id=content_id)
    return render(request, "blog/content_detail.html",{"contents":content})


