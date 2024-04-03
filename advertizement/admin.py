from django.contrib import admin
from .models import AdvertizementFirst, AdvertizementSecond, AdvertizementThird, Favicon
from msigana_ecommerce.admin_site import admin_site

class AdvertizementFirstAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AdvertizementFirst.objects.exists():
            return False
        return super().has_add_permission(request)
class AdvertizementSecondAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AdvertizementSecond.objects.exists():
            return False
        return super().has_add_permission(request)
    
class AdvertizementThirdAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AdvertizementThird.objects.exists():
            return False
        return super().has_add_permission(request)

class FaviconAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Favicon.objects.exists():
            return False
        return super().has_add_permission(request)
    
admin_site.register(AdvertizementFirst, AdvertizementFirstAdmin)
admin_site.register(AdvertizementSecond, AdvertizementSecondAdmin)
admin_site.register(AdvertizementThird, AdvertizementThirdAdmin)
admin_site.register(Favicon, FaviconAdmin)