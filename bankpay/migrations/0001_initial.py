# Generated by Django 5.0.1 on 2024-04-08 08:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paywithbank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('out_trade_no', models.CharField(editable=False, max_length=60)),
                ('transaction_no', models.CharField(blank=True, max_length=100)),
                ('payment_status', models.BooleanField(default=True)),
                ('screenshot', models.ImageField(upload_to='images/bank')),
                ('bank_name', models.CharField(max_length=200)),
                ('ref_number', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
