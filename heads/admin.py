# admin.py
from django.contrib import admin
from .models import HeadContent

class HeadContentAdmin(admin.ModelAdmin):
    list_display = ('content',)

    def has_add_permission(self, request):
        # if HeadContent object already exists, do not allow new ones to be added
        if HeadContent.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(HeadContent, HeadContentAdmin)