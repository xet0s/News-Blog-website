from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Etiket Sınıfı
class Tag(models.Model):
    name=models.CharField(max_length=25, unique=True) #Etiket ismi ve Unique(Benzersiz) Key Belirtisi
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        ordering=["name"]           #Nasıl sıralanacağı
        verbose_name= "Tag"         #Tekil isim
        verbose_name_plural="Tags"  #Çoğul isim
        db_table="tag"              #Veri Tabanı kayıt adı


#İçerik sınıfı
class Content(models.Model):
    
    
    title=models.CharField(max_length=255)                      #İçerik Başlığı
    content=models.TextField()                                  #İçerik
    created_at=models.DateTimeField(auto_now_add=True)          #İlk oluşma tarihi

    author=models.ForeignKey(User,on_delete=models.CASCADE)     #content-user bağlantısı
    post_tag=models.ForeignKey(Tag, on_delete=models.CASCADE)   #tag-content bağlantısı

    admin_approve=models.BooleanField(default=False)            #admin onay

    def __str__(self):
        return self.title
    
    class Meta:

        ordering=["-created_at"]                                #nasıl sıralanacağını belirleyen kısım
     