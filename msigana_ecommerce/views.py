from django.shortcuts import render
from store.models import Product
from users.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
import os

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
def new_arrivals(request):
    products = Product.objects.all().filter(product_is_available=True)
    context = {
        'products': products
    }
    return render(request, 'new-arrivals.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return JsonResponse({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user.phone_number,
                'address': user.address,
            })
    else:
        form = ProfileForm(instance=request.user)
    orders = request.user.order_set.order_by('-order_date')[:6]
    liked_products = request.user.liked_products.all()

    return render(request, 'profile.html', {'form': form, 'orders': orders, 'liked_products': liked_products})

def ads_txt(request):
    # Path to the Ads.txt file
    ads_txt_path = os.path.join(settings.BASE_DIR, '../static', 'Ads.txt')

    # Read the contents of the Ads.txt file
    with open(ads_txt_path, 'r') as f:
        ads_txt_content = f.read()

    # Return the contents of the Ads.txt file as the HTTP response
    return HttpResponse(ads_txt_content, content_type='text/plain')