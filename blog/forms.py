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