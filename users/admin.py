from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class StaffUser(CustomUser):
    class Meta:
        proxy = True

class CustomerUser(CustomUser):
    class Meta:
        proxy = True

class NoAddUserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

class StaffUserAdmin(NoAddUserAdmin):  # Use admin.ModelAdmin instead of UserAdmin
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = StaffUser
    list_display = ("email", "first_name", "last_name", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Social Links", {"fields": ("facebook_url", "telegram_url", "whatsapp_url")}),
    )
    add_fieldsets = (
        (None, {
             "classes": ("wide",),
             "fields": (
                 "email", "password1", "password2", "is_staff",
                 "is_active", "groups", "user_permissions", "first_name", "last_name"
             )}
        ),
        ("Social Links", {
            "fields": ("facebook_url", "telegram_url", "whatsapp_url")}
        ),
   )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    def get_queryset(self, request):
        return self.model.objects.filter(is_staff=True)

class CustomerUserAdmin(NoAddUserAdmin):  # Use admin.ModelAdmin instead of UserAdmin
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    list_display = ("email","address","point_reward","phone_number", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "point_reward")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2",
                "is_active", "groups", "user_permissions", "first_name", "last_name"
            )}
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    
    def get_queryset(self, request):
        return self.model.objects.filter(is_staff=False)
    

admin.site.register(StaffUser, StaffUserAdmin)  # Register the admin for staff
admin.site.register(CustomerUser, CustomerUserAdmin)  # Register the default admin for customers
