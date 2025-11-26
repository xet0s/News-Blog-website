from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [

    path('', views.content_list, name="content_list"),                         #İçerik listesini gösteren sayfa url'si

    path('content/<slug:slug>/',views.content_detail,name="content_detail"),   #İçerik detaylarını gösteren sayfa url'si

    path('tag/<slug:tag_slug>', views.content_by_tag,name="content_by_tag"),    #filtre

    path("add_content/",blog_views.add_content,name="add_content"),     #içerik ekleme ekranı
    
    path("profile/",blog_views.profile,name="profile"),             #profil ekranı
    path("profile/edit/",blog_views.update_profile,name="update_profile"),#profil düzenleme

    path('update_content/<int:content_id>/', blog_views.update_content, name='update_content'),#içerik düzenleme
    
    path('hakkimizda/', blog_views.about, name='about'),#Hakkımda

]