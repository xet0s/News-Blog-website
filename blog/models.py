from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


#Etiket Sınıfı
class Tag(models.Model):
    name=models.CharField(max_length=25, unique=True) #Etiket ismi ve Unique(Benzersiz) Key Belirtisi
    
    slug=models.SlugField(max_length=25,unique=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=  slugify(self.name)
        super().save(*args,**kwargs)
    
    class Meta:
        
        ordering=["name"]           #Nasıl sıralanacağı
        verbose_name= "Tag"         #Tekil isim
        verbose_name_plural="Tags"  #Çoğul isim
        db_table="tag"              #Veri Tabanı kayıt adı


#İçerik sınıfı
class Content(models.Model):
    
    
    title=models.CharField(max_length=255)                      #İçerik Başlığı
    content=models.TextField()                                  #İçerik
    image=models.ImageField(upload_to='blog_images/',blank=True,null=True)#Görsel Ekleme
    created_at=models.DateTimeField(auto_now_add=True)          #İlk oluşma tarihi
    slug=models.SlugField(max_length=255,unique=True,blank=True)#Linksel başlık
    author=models.ForeignKey(User,on_delete=models.CASCADE)     #content-user bağlantısı
    post_tag=models.ForeignKey(Tag, on_delete=models.CASCADE)   #tag-content bağlantısı

    admin_approve=models.BooleanField(default=False)            #admin onay

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) 
        super().save(*args, **kwargs)
    class Meta:

        ordering=["-created_at"]                                #nasıl sıralanacağını belirleyen kısım

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True,null=True)
    def __str__(self):
        return f"{self.user.username} Profili"
