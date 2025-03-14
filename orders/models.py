from django.db import models
import uuid
import time
import random
import string
from users.models import CustomUser
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('in_progress', 'In Progress'),
        ('complete', 'Completed'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    order_phone = models.CharField(max_length=13, blank=True)
    order_username = models.CharField(max_length=50, blank=True,null=True)
    order_address = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total_prices = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    outTradeNo = models.CharField(max_length=60, editable=False)
    transaction_no = models.CharField(max_length=60, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    referral_code = models.CharField(max_length=30, blank=True)
    order_key = models.CharField(max_length=6, editable=False, unique=True)
    paid_by_points = models.BooleanField(default=False)
    paid_by_telebirr = models.BooleanField(default=False)
    paid_by_bank = models.BooleanField(default=False)
    bank_ref_number = models.CharField(max_length=200, blank=True)


    def save(self, *args, **kwargs):
        if not self.order_key:
            while True:
                letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
                numbers = ''.join(random.choice(string.digits) for _ in range(3))
                self.order_key = letters + numbers
                if not Order.objects.filter(order_key=self.order_key).exists():
                    break

        if not self.outTradeNo:
           self.outTradeNo = str(int(time.time() * 1000)) + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.order_key)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_size = models.CharField(max_length=100, blank=True)
    product_color = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()
    delivered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.product_owner = self.product.product_owner
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product_name} ({self.quantity})'