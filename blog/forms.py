from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django                     import forms
from django.forms import ModelForm
from .models import Content,Profile
from django_summernote.widgets import SummernoteWidget

class UserRegisterForm(UserCreationForm): #Django nun kendi kayıt class'ı

    class Meta:         #istenilen alanlar
        model  = User
        fields = ["username","email"]   #gerekli veriler

class ContentForm(ModelForm):
    class Meta:
        model=Content

        fields=["title","content","post_tag","image"] # Yazar, onay, ve oluşturma tarihi otomatik olduğu için formda görünmez
        widget = {                            #Html de kullanacağımız kutuların hazır hali
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Haber Başlığını buraya giriniz'
            }),
            'content':SummernoteWidget(attrs={
                'class':'form-content',
                'placeholder':'Haber içeriğini giriniz'
            }),
            
            'post_tag':forms.Select(attrs={
                'class':'form-select'
            }),
            'image':forms.FileInput(attrs={
                'class':'form-control',
                'id':'id_image'
            }),
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio']

        widgets={
            'bio':forms.Textarea(attrs={
                'class':'form-control',
                'rows':4,
                'placeholder':'Kendinizle ilgili paylaşmak istediklerinizi belirtiniz'
            }),
        }
