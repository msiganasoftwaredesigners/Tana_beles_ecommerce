#orders/models.py
from django.db import models
import uuid

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    order_phone = models.CharField(max_length=13)
    order_email = models.EmailField(max_length=50, blank=True, null=True)
    order_address = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    order_total_prices = models.DecimalField(max_digits=10, decimal_places=2)
    order_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    payment_status = models.BooleanField(default=False)