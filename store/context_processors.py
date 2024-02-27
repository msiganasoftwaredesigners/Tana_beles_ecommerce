from django.utils import timezone
from datetime import timedelta
from django.core.cache import cache
from .models import Product
from django.db.models import Count, Q

# def most_liked_products(request):
#     # Try to fetch the most liked products from cache
#     most_liked_products = cache.get('most_liked_products')

#     # If the most liked products are not in cache, calculate them
#     if most_liked_products is None:
#         # Get the date 90 days ago
#         ninety_days_ago = timezone.now() - timedelta(days=90)

#         # Get the most liked products in the last 90 days
#         most_liked_products = Product.objects.filter(
#             product_modified_date__gte=ninety_days_ago
#         ).annotate(
#             likes_count=Count('likes')
#         ).order_by('-likes_count')[:10]

#         # Store the most liked products in cache for 3 days
#         cache.set('most_liked_products', most_liked_products, 60)
#         #cache.set('most_liked_products', most_liked_products, 60*60*24*1)

#     return {'most_liked_products': most_liked_products}
def most_liked_products(request):
    # Try to fetch the most liked products from cache
    most_liked_products = cache.get('most_liked_products')

    # If the most liked products are not in cache, calculate them
    if most_liked_products is None:
        # Get the date 90 days ago
        ninety_days_ago = timezone.now() - timedelta(days=90)

        # Get the most liked products in the last 90 days
        most_liked_products = Product.objects.filter(
            product_modified_date__gte=ninety_days_ago
        ).annotate(
            likes_count=Count('likes')
        ).order_by('-likes_count')[:8]

        # Store the most liked products in cache for 3 days
        cache.set('most_liked_products', most_liked_products, 60)
        #cache.set('most_liked_products', most_liked_products, 60*60*24*1)
    else:
        # Check if the products in cache still exist in the database
        most_liked_products = [product for product in most_liked_products if Product.objects.filter(id=product.id).exists()]

    return {'most_liked_products': most_liked_products}