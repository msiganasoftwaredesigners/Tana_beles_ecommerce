# Generated by Django 5.0.1 on 2024-04-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_order_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_email',
        ),
        migrations.AddField(
            model_name='order',
            name='order_username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
