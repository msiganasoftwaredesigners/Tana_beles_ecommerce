# Generated by Django 5.0.1 on 2024-02-23 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_size', models.CharField(blank=True, max_length=100)),
                ('product_color', models.CharField(blank=True, max_length=100)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
        ),
    ]
