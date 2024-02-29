#msigana_ecommerce/views.py
from django.shortcuts import render, HttpResponseRedirect
from store.models import Product
# from django.contrib.auth import logout
# from django.shortcuts import redirect
from users.forms import ProfileForm
from django.contrib.auth.decorators import login_required


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

# def users_profiles(request):
#     return render(request, 'profile.html')


# msigan_ecommerce/views.py
# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/accounts/profile/')
#     else:
#         form = ProfileForm(instance=request.user)

#     liked_products = request.user.liked_products.all()

#     return render(request, 'profile.html', {'form': form, 'liked_products': liked_products})

from django.http import JsonResponse

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

    liked_products = request.user.liked_products.all()

    return render(request, 'profile.html', {'form': form, 'liked_products': liked_products})