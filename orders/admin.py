# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem
from .export_to_gsheets import export_orders_to_gsheets
from django.urls import path, reverse
from django.http import HttpResponseRedirect   
from .views import export_orders_view 
from msigana_ecommerce.admin_site import admin_site
from django.urls import reverse
from django.utils.html import format_html
from bankpay.models import Paywithbank
def export_selected_orders_to_gsheets(modeladmin, request, queryset):
    export_orders_to_gsheets(queryset)
export_selected_orders_to_gsheets.short_description = "Export selected orders to Google Sheets"


class OrderItemInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = OrderItem
    extra = 0  # Number of extra forms to display
    fields = ('delivered','product_link', 'product_owner_username', 'product_name', 'product_price', 'product_size', 'product_color', 'quantity', 'product_brand')
    readonly_fields = ['product_link', 'product_owner_username', 'product_name', 'product_price', 'product_size', 'product_color', 'quantity', 'product_brand']
   
    def product_owner_username(self, instance):
        return instance.product.product_owner.username
    product_owner_username.short_description = 'Product Owner'

    def has_change_permission(self, request, obj=None):
        return True
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields
        return self.readonly_fields + ('delivered',)

    def product_link(self, instance):
        url = reverse("admin:store_product_change", args=[instance.product.id])
        return format_html('<a href="{}">{}</a>', url, instance.product)
    product_link.short_description = 'Product'

    def has_add_permission(self, request, obj=None):
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
    list_display = ['first_name',  'payment_status','status', 'bank_ref_number','paid_by_bank', 'paid_by_telebirr','paid_by_points',  'order_phone', 'order_username', 'order_total_prices', 'order_address',  'order_date',  'outTradeNo', 'last_name']
    list_filter = ['order_date', 'payment_status', 'status', 'paid_by_telebirr','paid_by_bank','paid_by_points']
    inlines = [OrderItemInline]
    readonly_fields = ['first_name', 'payment_status', 'order_phone', 'order_username', 'order_date', 'bank_ref_number', 'order_total_prices', 'order_address', 'transaction_no', 'bank_ref_number', 'user', 'paid_by_points', 'paid_by_telebirr', 'last_name', 'referral_code']
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
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or (request.user.is_authenticated and request.user.is_ordersuperuser):
            return qs
        return qs.filter(items__product__product_owner=request.user)
    

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model method to save the object
        super().save_model(request, obj, form, change)

        # Check if the 'paid_by_bank' field has changed
        if 'paid_by_bank' in form.changed_data:
            try:
                paywithbank_obj = Paywithbank.objects.get(transaction_no=obj.transaction_no)
                paywithbank_obj.paid_by_bank = obj.paid_by_bank

                # Update payment status based on paid_by_bank value
                if obj.paid_by_bank:
                    paywithbank_obj.payment_status = True  # Assuming payment status should be True if paid by bank
                else:
                    paywithbank_obj.payment_status = False  # Assuming payment status should be False if not paid by bank

                paywithbank_obj.save()
                #Update payment status in Order model
                if obj.payment_status != paywithbank_obj.payment_status:
                    obj.payment_status = paywithbank_obj.payment_status
                    obj.save()
            except Paywithbank.DoesNotExist:
                # Handle the case where Paywithbank object does not exist for this order
                pass


admin_site.register(Order, OrderAdmin)