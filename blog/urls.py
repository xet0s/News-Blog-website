from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [

    path('', views.content_list, name="content_list"),                         #İçerik listesini gösteren sayfa url'si

    path('content/<int:content_id>/',views.content_detail,name="content_detail"),   #İçerik detaylarını gösteren sayfa url'si

    path('tag/<slug:tag_slug>', views.content_by_tag,name="content_by_tag"),    #filtre

    path("icerik_ekle/",blog_views.add_content,name="add_content"),

]