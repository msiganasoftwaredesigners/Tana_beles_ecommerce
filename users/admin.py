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

class StaffUserAdmin(admin.ModelAdmin):  # Use admin.ModelAdmin instead of UserAdmin
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = StaffUser
    list_display = ("email", "first_name", "last_name", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "first_name", "last_name"
            )}
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    def get_queryset(self, request):
        return self.model.objects.filter(is_staff=True)

class CustomerUserAdmin(admin.ModelAdmin):  # Use admin.ModelAdmin instead of UserAdmin
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    list_display = ("email", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
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
