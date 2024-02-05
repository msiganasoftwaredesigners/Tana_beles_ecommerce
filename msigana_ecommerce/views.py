from django.shortcuts import render
from store.models import Product
# from django.contrib.auth import logout
# from django.shortcuts import redirect

def home(request):
    products = Product.objects.all().filter(product_is_available=True)
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about-us.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def users_profiles(request):
    return render(request, 'profile.html')
