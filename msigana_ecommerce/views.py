from django.shortcuts import render
from store.models import Product
from users.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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
    orders = request.user.order_set.filter(payment_status=True).order_by('-order_date')[:6]
    liked_products = request.user.liked_products.all()

    return render(request, 'profile.html', {'form': form, 'orders': orders, 'liked_products': liked_products})