from django.contrib import admin
from .models import Footer

class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if Footer object already exists, do not allow new ones to be added
        if Footer.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(Footer, FooterAdmin)