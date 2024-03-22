# admin.py
from django.contrib import admin
from .models import PaymentNotification

@admin.register(PaymentNotification)
class PaymentNotificationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    list_display = ['msisdn', 'out_trade_no', 'total_amount', 'trade_date', 'trade_no', 'trade_status', 'transaction_no']
