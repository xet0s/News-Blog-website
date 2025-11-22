from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django                     import forms
from django.forms import ModelForm
from .models import Content

class UserRegisterForm(UserCreationForm): #Django nun kendi kayıt class'ı

    class Meta:         #istenilen alanlar
        model  = User
        fields = ["username","email"]   #gerekli veriler

class ContentForm(ModelForm):
    class Meta:
        model=Content

        fields=["title","content","post_tag"] # Yazar, onay, ve oluşturma tarihi otomatik olduğu için formda görünmez
        widget = {                            #Html de kullanacağımız kutuların hazır hali
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Haber Başlığını buraya giriniz'
            }),
            'content':forms.Textarea(attrs={
                'class':'form-control',
                'rows':15,
                'placeholder':'Haber detaylarını buraya giriniz'
            }),
            'post_tag':forms.Select(attrs={
                'class':'form-select'
            }),
            'image':forms.FileInput(attrs={
                'class':'form-control',
                'id':'id_image'
            }),
        }