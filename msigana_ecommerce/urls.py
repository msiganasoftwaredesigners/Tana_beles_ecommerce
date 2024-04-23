from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from msigana_ecommerce.admin_site import admin_site
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve

# from django.contrib import admin

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.home, name='home'),
    path('new-arrivals/', views.new_arrivals, name='new-arrivals'),
    path('store/', include('store.urls')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('blog/', include('blog.urls')),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
    path('telebirrpay/', include('telebirrpay.urls')),
    path('rewardpay/', include('rewardpay.urls')),
    path('bankpay/', include('bankpay.urls')),
    
    path("accounts/profile/", views.update_profile, name="users_profiles"),
    path('googleeb174eafe2c6e97d.html', TemplateView.as_view(template_name='googleeb174eafe2c6e97d.html')),
    path('ads.txt', views.ads_txt, name='ads_txt'),

]
# admin.site.site_header = 'Tanabeles Login'

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media setup

