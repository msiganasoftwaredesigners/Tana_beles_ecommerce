#orders/models.py
from django.db import models
import uuid

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('in_progress', 'In Progress'),
        ('complete', 'Completed'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    order_phone = models.CharField(max_length=13)
    order_email = models.EmailField(max_length=50, blank=True)
    order_address = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    order_total_prices = models.DecimalField(max_digits=10, decimal_places=2)
    order_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    payment_status = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')

    def __str__(self):
        return str(self.order_key)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_size = models.CharField(max_length=100, blank=True)
    product_color = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} ({self.quantity})'