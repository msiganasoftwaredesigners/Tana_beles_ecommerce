# Generated by Django 5.0.1 on 2024-02-21 16:36

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('selected_size', models.CharField(blank=True, max_length=100)),
                ('selected_pirce', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('selected_color', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
            ],
        ),
    ]
