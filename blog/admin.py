from django.contrib import admin
from .models import Category,Post


# For configuration of Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

# For configuration of Post Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js=('https://cdn.tiny.cloud/1/6lcey780j5svbsoe5rrp5eexxaflqer5s38jluhtmel3cqpn/tinymce/6/tinymce.min.js','js/script.js',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
