from . import views
from django.urls import path


urlpatterns = [

    path('', views.content_list, name="content_list"),                         #İçerik listesini gösteren sayfa url'si

    path('content/<int:Content_id>/',views.content_detail,name="content_detail"),   #İçerik detaylarını gösteren sayfa url'si

]