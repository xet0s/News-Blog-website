from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .models import Content,Tag
from .forms import UserRegisterForm, ContentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import ProfileUpdateForm,ContentForm
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
        print("GELEN DOSYALAR:", request.FILES)

        form=ContentForm(request.POST, request.FILES)

        if form.is_valid():
            content_instance=form.save(commit=False)#ilk onay durumunu atar
            content_instance.author= request.user   #Yazar
            content_instance.admin_approve= False   #Onay durumu
            content_instance.save()                 #kayıt
            

            form.save_m2m()                         #tag ilişkisi

            messages.success(request,"İçerik kaydedildi. Onay bekleniyor")
            return redirect('content_list')
    else:
        form=ContentForm()
    return render(request, "blog/add_content.html",{"form":form}) #template gönderir

@login_required
def update_content(request,content_id):#Varolan içerikleri tekrar düzenlemeyi sağlayan fonksiyon
    content=get_object_or_404(Content,id=content_id)
    if content.author !=request.user:
        raise PermissionDenied("Bu içeriği düzenleme yetkiniz yok")
    
    if request.method=="POST":
        form=ContentForm(request.POST,request.FILES,instance=content)
        if form.is_valid():
            if not form.has_changed():
                return redirect('profile')
            content_instance=form.save(commit=False)
            content_instance.admin_approve=False

            content_instance.save()
            form.save_m2m()

            messages.success(request,"İçerik Güncellendi ve Tekrar Onaya Düştü")
            return('profile')
    else:
        form=ContentForm(instance=content)
    return render(request,'blog/add_content.html',{
        "form":form,
        "title":"İçerik Düzenle"
    })
@login_required
def profile(request):#Profil ekranı ve editörlerin içeriklerini getiren fonksiyon
    user_contents=  Content.objects.filter(author=request.user).order_by("created_at")
    return render(request,"blog/profile.html",{
        "user_contents":user_contents
    })

@login_required
def update_profile(request):#Profil düzenlemeyi sağlayan fonksiyon
    if request.method=="POST":
        form=ProfileUpdateForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.success(request,"Profil başarıyla güncellendi")
            return redirect("profile")
    else:
        form=ProfileUpdateForm(instance=request.user.profile)

    return render(request,"blog/update_profile.html",{
        "form":form,
        })