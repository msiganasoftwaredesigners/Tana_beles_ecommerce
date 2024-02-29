from django.contrib import admin
from .models import Post

from django.utils.text import slugify
from django.utils.html import strip_tags

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(strip_tags(obj.title))
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)