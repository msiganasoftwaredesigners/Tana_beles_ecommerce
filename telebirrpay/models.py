# models.py
from django.db import models

class PaymentNotification(models.Model):
    msisdn = models.CharField(max_length=20)
    out_trade_no = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    trade_date = models.DateTimeField()
    trade_no = models.CharField(max_length=100, unique=True)
    trade_status = models.IntegerField()
    transaction_no = models.CharField(max_length=100)

    def __str__(self):
        return self.out_trade_no
