from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Product,Like
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from .context_processors import most_liked_products

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.filter(category=categories, product_is_available=True).prefetch_related('images').order_by('product_created_date')
    else:
        products = Product.objects.filter(product_is_available=True).prefetch_related('images').order_by('-product_created_date')

    most_liked_products_with_count = most_liked_products(request)['most_liked_products']
    
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
        data = {"products": list(products_page), "end": False}
        return JsonResponse(data, safe=False)

    # Your existing code
    most_liked_product = most_liked_products_with_count[0] if most_liked_products_with_count else None
    return render(request, 'index.html', {'products': products_page, 'most_liked_product': most_liked_product})

def product_detail(request, category_slug, product_slug):
    try:
        single_product = get_object_or_404(Product, category__category_slug=category_slug, product_slug=product_slug)
        single_product.increment_views()
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        main_image = single_product.images.filter(is_main=True).first()
        other_images = single_product.images.all()
        related_products = Product.objects.filter(category=single_product.category).exclude(id=single_product.id).order_by('-product_created_date')[:4]
        color_variations = single_product.variations.filter(color__isnull=False)
        size_variations = single_product.variations.filter(size__isnull=False)
        

        is_owner = request.user == single_product.product_owner
        # like Implementation
        product_slug = single_product.product_slug
        
        liked = False
        if request.user.is_authenticated:
            liked = Like.objects.filter(product=single_product, liked_by=request.user).exists()
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
        'related_products': related_products,
        'color_variations': color_variations,
        'size_variations': size_variations,
        'liked': liked,
        'is_owner': is_owner,
    }
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked})
    
    return render(request, 'product-detail.html', context)


@login_required
def like_product(request, product_slug):
    product = get_object_or_404(Product, product_slug=product_slug)
    user = request.user

    if request.method == "POST":
        # Check if the user has already liked the post
        if product.product_likes.filter(liked_by=user).exists():
            # User has already liked the post, so remove the like
            Like.objects.filter(product=product, liked_by=user).delete()
            liked = False  # Indicate that the post is unliked
        else:
            # User has not liked the post, so create a new like
            Like.objects.create(product=product, liked_by=user)
            liked = True  # Indicate that the post is liked

        # Update the product_likes_count field on the product
        product.product_likes_count = product.product_likes.count()
        product.save()

        # Prepare the response data
        response_data = {
            "liked": liked,
            "likes_count": product.product_likes_count,
        }

        return JsonResponse(response_data)

    return redirect("product-detail", category_slug=product.category.category_slug, product_slug=product_slug)

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