# admin.py
from django.contrib import admin
from .models import PaymentNotification
from msigana_ecommerce.admin_site import admin_site


class PaymentNotificationAdmin(admin.ModelAdmin):
    list_display = ['msisdn', 'out_trade_no', 'total_amount', 'trade_date', 'trade_no', 'trade_status', 'transaction_no']
    list_filter = ['trade_date', 'trade_status']
    
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin_site.register(PaymentNotification, PaymentNotificationAdmin)