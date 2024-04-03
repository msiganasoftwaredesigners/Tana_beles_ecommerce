from django.contrib import admin
from .models import Cart, CartItem
from msigana_ecommerce.admin_site import admin_site

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    readonly_fields = ('product', 'cart', 'quantity', 'is_active', 'selected_size', 'selected_price', 'selected_color', 'category', 'product_image_url', 'product_brand', 'product_name')

admin_site.register(Cart, CartAdmin)
admin_site.register(CartItem, CartItemAdmin)
