# orders/admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_key', 'first_name', 'last_name', 'order_phone', 'order_total_prices', 'order_date', 'payment_status')

admin.site.register(Order, OrderAdmin)