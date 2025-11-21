from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .models import Content,Tag
from .forms import UserRegisterForm, ContentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
ITEM_PER_PAGE=6 #Her sayfada gösterilecek post miktarı

def content_list(request): #Bütün içerikleri çeken fonksiyon

    content= Content.objects.filter(admin_approve=True).order_by('-created_at')

    paginator=Paginator(content, ITEM_PER_PAGE) #anasayfa içerik sayfalandırma
    page_number=request.GET.get('page')         #sayfa sayısı
    page_obj = paginator.get_page(page_number)  #içeriğin bulunduğu sayfayı kontrol eden sistem


    return render(request,"blog/content_list.html", {"contents":page_obj,"current_tag":None})

def content_by_tag(request,tag_slug): #tag/etikete göre içerik filtreleme sistemi

    filter_tag=get_object_or_404(Tag,slug=tag_slug) #filtreleme yoksa hata kodu verme
    filtered_contents = Content.objects.filter(post_tag=filter_tag,admin_approve=True).order_by('-created_at')#admin onay filtresi
    filtered_contents= Content.objects.filter(post_tag=filter_tag) #filtrelenmiş içerikler
    paginator=Paginator(filtered_contents,ITEM_PER_PAGE)#sayfalama sistemini ekleme
    page_number=request.GET.get("page")                 #sayfa sayısı
    page_obj=paginator.get_page(page_number)   #filtrelenemiş içeriğin bulunduğu sayfayı kontrol eden sistem

    return render(request,"blog/content_list.html", { 
        "contents":page_obj,
        "current_tag":filter_tag
    }) 

def content_detail(request, content_id): #İçerik detaylarını çeken fonksiyon
    content= get_object_or_404(Content, id=content_id)
    return render(request, "blog/content_detail.html",{"content":content})



def register(request):
    if request.method == "POST": #kullanıcı POST 
        form= UserRegisterForm(request.POST)

        if form.is_valid(): # Form geçerli mi diye test eden fonksiyon
            form.save()     # db kayıt 
            username= form.cleaned_data.get("username")

            messages.success(request,f'Hesap oluşturuldu: {username},Giriş yapabilirsiniz') #Başarı mesajı
            return redirect("login") # Giriş sayfasına yönlendirme
    else:
        form = UserRegisterForm()#boş form oluşturma
    return render(request, "blog/register.html", {"form":form} ) #Template kısmına 'form'  adıyla veri yollama

@login_required
def add_content(request):
    if not request.user.groups.filter(name="editor").exists():#kullanıcı yetki kontrolü
        raise PermissionDenied("İçerik eklemek için yetkiniz bulunmamaktadır. Editor olamazsınız.")
    
    if request.method== "POST":
        form=ContentForm(request.POST,request.FILES)

        if form.is_valid():
            content_instance=form.save(commit=False)#ilk onay durumunu atar
            content_instance.author= request.user   #Yazar
            content_instance.admin_approve= False   #Onay durumu
            content_instance.save()                 #kayıt
        
            form.save_m2m()#tag ilişkisi

            messages.success(request,"İçerik kaydedildi. Onay bekleniyor")
    else:
        form=ContentForm()
    return render(request, "blog/add_content.html",{"form":form}) #template gönderir