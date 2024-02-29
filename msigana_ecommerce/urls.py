# msigana_ecommerce/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('blog/', include('blog.urls')),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
    
    path("accounts/profile/", views.update_profile, name="users_profiles"),
    # path("__reload__/", include("django_browser_reload.urls")),
]
admin.site.site_header = 'Tanabeles Login'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media setup
