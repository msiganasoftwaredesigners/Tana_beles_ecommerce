# Generated by Django 5.0.1 on 2024-03-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telebirrpay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentnotification',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
