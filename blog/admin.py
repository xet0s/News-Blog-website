from django.contrib import admin
from .models import Tag, Content
# Register your models here.


@admin.register(Tag)
class admin_Tag(admin.ModelAdmin):
    list_display=("name",)           #admin panelinde tag çağrıldığında görünecek kisim
    search_fields=("name",)          #arama filtresi
    fields = ('title', 'content', 'post_tag', 'admin_approve')
    def save_model(self, request, obj, form, change):
        if not obj.pk: # Yeni bir nesne oluşturuluyorsa
            obj.author = request.user # Yazar, o an giriş yapan kullanıcıdır
        super().save_model(request, obj, form, change)

@admin.register(Content)
class admin_Content(admin.ModelAdmin):
    list_display=("title","admin_approve","created_at")         #admin panelinde content çağrıldığında görünecek kisim
    list_filter=("admin_approve",)                              #admin panelinde content yayın kısmını filtreleyen kısım
    search_fields=("title","author__username","post_tag__name") #arama filtresi

