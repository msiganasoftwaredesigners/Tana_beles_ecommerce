from django.contrib import admin
from .models import RewardRate, PaywithReward

class RewardRateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if RewardRate.objects.exists():
            return False
        return super().has_add_permission(request)


class PaywithRewardAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
    list_display = ['user', 'total_amount', 'payment_date', 'payment_status']
    list_filter = ['payment_date', 'payment_status']
    search_fields = ['user', 'total_amount', 'payment_date', 'payment_status']
    list_per_page = 30

admin.site.register(RewardRate, RewardRateAdmin)
admin.site.register(PaywithReward, PaywithRewardAdmin)