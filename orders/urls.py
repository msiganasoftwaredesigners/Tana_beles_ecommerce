# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_complete/', views.order_complete, name='order_complete'),
]