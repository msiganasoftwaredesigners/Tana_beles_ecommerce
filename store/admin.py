from django.contrib import admin
from store.models import Product, Variation, Color, Size, ProductImage, SizeVariation
from django.core.cache import cache
import nested_admin

class VariationInline(nested_admin.NestedTabularInline):
    model = Variation
    fields = ('color','is_active')
    max_num = 1
    can_delete = False


    def get_extra(self, request, obj=None, **kwargs):
        extra = 1 if obj is None else 0
        return extra
    
class SizeVariationInline(nested_admin.NestedTabularInline):
    model = SizeVariation
    fields = ('size', 'price')
    inlines = [VariationInline]

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1 if obj is None else 0
        return extra

class ProductImageInline(nested_admin.NestedTabularInline):
    model = ProductImage
    fields = ('image', 'is_main')
    
    def get_extra(self, request, obj=None, **kwargs):
        extra = 2 if obj is None else 0
        return extra
    
class ProductAdmin(nested_admin.NestedModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = (
        'product_name','likes_count','product_phone', 'product_stock', 'category',
        'product_created_date', 'product_modified_date', 'product_is_available',
        'display_sizes'  # Custom methods for display
    )
    inlines = [SizeVariationInline, ProductImageInline]

    class Media:
        js = ('js/admin.js',)

    def display_colors(self, obj):
        return ", ".join([var.color.name for size_var in obj.sizevariation_set.all() for var in size_var.variation_set.all() if var.color and var.color.name])
    def display_sizes(self, obj):
        return ", ".join([size_var.size.name for size_var in obj.sizevariation_set.all() if size_var.size])
    
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Likes Count'

    def save_model(self, request, obj, form, change):
        if not change:  # the object is being created, so set the user
            obj.product_owner = request.user
        obj.save()

    def delete_model(self, request, obj):
        # Clear the most liked products cache
        cache.delete('most_liked_products')

        # Call the original delete method
        super().delete_model(request, obj)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(product_owner=request.user)
        return qs
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # remove the email field from the form if the user is not a superuser
        if not request.user.is_superuser:
            form.base_fields.pop('product_owner', None)
        return form
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)






