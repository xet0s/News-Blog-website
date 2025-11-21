from .models import Tag

def get_all_tag(request):
    all_tags=Tag.objects.all().order_by("name")[:20]

    return {"ALL_TAGS":all_tags}