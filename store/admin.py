from django.contrib import admin
from store.models import Product, Variation, Color, Size, ProductImage

class VariationInline(admin.TabularInline):
    model = Variation


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image', 'is_main')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = (
        'product_name', 'product_stock', 'category',
        'product_created_date', 'product_modified_date', 'product_is_available',
        'display_colors', 'display_sizes'  # Custom methods for display
    )
    inlines = [VariationInline, ProductImageInline]

    class Media:
        js = ('js/admin.js',)

    def display_colors(self, obj):
        return ", ".join([var.color.name for var in obj.variations.all() if var.color])

    def display_sizes(self, obj):
        return ", ".join([var.size.name for var in obj.variations.all() if var.size])

admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)