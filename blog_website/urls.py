"""
URL configuration for blog_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog import views as blog_views
urlpatterns = [
    path('admin/', admin.site.urls),#admin panel

    path("",include("blog.urls")),  #ana site url'si
    path('kayit/', blog_views.register, name='register'),   #Kayıt yolu
    path("giris/", auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"), #giriş yolu
    path("cikis/", auth_views.LogoutView.as_view(next_page="/"),name="logout"),#çıkış yolu
    path("içerik_duzenle/<int:content_id>/", blog_views.update_content,name="update_content"), #içerik düzenleme yolu
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS[0])