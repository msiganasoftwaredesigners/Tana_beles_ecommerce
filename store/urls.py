from django.urls import path
from store import views
from .views import like_product

urlpatterns = [
    path('', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-complete/', views.order_complete, name='order_complete'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
    path('product/<slug:product_slug>/like/', like_product, name='like_product'),
    

]