# Generated by Django 5.0.1 on 2024-04-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_order_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bank_ref_number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
