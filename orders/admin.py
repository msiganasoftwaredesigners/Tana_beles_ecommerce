# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem
from .export_to_gsheets import export_orders_to_gsheets
from django.urls import path, reverse
from django.http import HttpResponseRedirect   
from .views import export_orders_view 


def export_selected_orders_to_gsheets(modeladmin, request, queryset):
    export_orders_to_gsheets(queryset)
export_selected_orders_to_gsheets.short_description = "Export selected orders to Google Sheets"


class OrderItemInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = OrderItem
    extra = 0  # Number of extra forms to display
    readonly_fields = ['product_name', 'product_price', 'product_size', 'product_color', 'quantity', 'product_brand']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

class OrderAdmin(admin.ModelAdmin):
    def export_selected_orders_pdf(self, request, queryset):
        return export_orders_view(request, queryset, 'pdf')
    export_selected_orders_pdf.short_description = "Export selected orders to PDF"

    def export_selected_orders_xlsx(self, request, queryset):
        return export_orders_view(request, queryset, 'xlsx')
    export_selected_orders_xlsx.short_description = "Export selected orders to XLSX"
    
    actions = [export_selected_orders_to_gsheets, export_selected_orders_pdf, export_selected_orders_xlsx]
    list_display = ['first_name', 'last_name', 'user', 'outTradeNo', 'order_phone', 'order_username', 'order_date', 'order_total_prices', 'order_address', 'payment_status', 'status']
    list_filter = ['order_date', 'payment_status', 'status']
    inlines = [OrderItemInline]
    readonly_fields = ['first_name', 'last_name', 'order_phone', 'order_username', 'order_date', 'order_total_prices', 'order_address', 'payment_status']

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def export_orders(self, request):
        return HttpResponseRedirect(reverse('export_orders'))

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('export_orders/', self.admin_site.admin_view(self.export_orders), name='export_orders'),
        ]
        return urls + custom_urls

admin.site.register(Order, OrderAdmin)