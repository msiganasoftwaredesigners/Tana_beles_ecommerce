from django.contrib import admin
from .models import GoogleAppsScript
from msigana_ecommerce.admin_site import admin_site

class GoogleAppsScriptAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return super().has_add_permission(request)

admin_site.register(GoogleAppsScript, GoogleAppsScriptAdmin)