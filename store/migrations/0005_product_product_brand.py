# Generated by Django 5.0.1 on 2024-01-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_product_images_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(blank=True, default='Unknown Brand', max_length=150),
        ),
    ]
