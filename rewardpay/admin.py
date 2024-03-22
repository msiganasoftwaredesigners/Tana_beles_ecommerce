from django.contrib import admin
from .models import RewardRate

class RewardRateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if RewardRate.objects.exists():
            return False
        return super().has_add_permission(request)
    
admin.site.register(RewardRate, RewardRateAdmin)
