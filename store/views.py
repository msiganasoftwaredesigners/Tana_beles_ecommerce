from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.filter(category=categories, product_is_available=True).prefetch_related('images').order_by('product_created_date')
    else:
        products = Product.objects.filter(product_is_available=True).prefetch_related('images').order_by('-product_created_date')

    paginator = Paginator(products, 12)
    page = request.GET.get('page')

    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"end": True}, status=404)  # If the page is not an integer deliver a 404 status
        products_page = paginator.page(1)
    except EmptyPage:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"end": True}, status=404)  # If the page is out of range deliver a 404 status
        products_page = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"products": list(products_page)}, safe=False)

    return render(request, 'store.html', {'products': products_page})

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__category_slug=category_slug, product_slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        main_image = single_product.images.filter(is_main=True).first()
        other_images = single_product.images.filter(is_main=False)
        related_products = Product.objects.filter(category=single_product.category).exclude(id=single_product.id).order_by('-product_created_date')[:4]
    except Exception as e:
        raise e
    
    color_dict = {
    'red': '#ff0000',
    'blue': '#0000ff',
    'green': '#008000',
    'yellow': '#ffff00',
    'orange': '#ffa500',
    'purple': '#800080',
    'black': '#000000',
    'white': '#ffffff',
    'gray': '#808080',
    'brown': '#a52a2a',
    'pink': '#ffc0cb',
    'gold': '#ffd700',
    'silver': '#c0c0c0',
    
    }
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'color_dict': color_dict,
        'main_image': main_image,
        'other_images': other_images,
        'related_products': related_products
    }
    return render(request, 'product-detail.html', context)


def search(request):
    context = {}
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('product_created_date').filter(
                Q(product_description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
            context = {
                'products': products,
                'product_count': product_count
            }

    return render(request, 'store.html', context)


def checkout(request):
    return render(request, 'checkout.html')

def order_complete(request):
    return render(request, 'order-complete.html')