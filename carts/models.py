from django.db import models
from store.models import Product
from uuid import uuid4


class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # to override the object name of this class
        return str(self.cart_id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True, db_index=True)
    selected_size = models.CharField(max_length=100, blank=True)
    selected_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    selected_color = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    product_image_url = models.URLField(blank=True)  # Add product image URL field
    product_brand = models.CharField(max_length=100, blank=True)
    product_name = models.CharField(max_length=100, blank=True)


    def each_product_total(self):
        return self.selected_price * self.quantity

    def __str__(self):
        return self.product.product_name

  