# Generated by Django 5.0.1 on 2024-04-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankpay', '0004_bankname_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='paywithbank',
            name='paid_by_bank',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='paywithbank',
            name='phone_number',
            field=models.CharField(default='0900000000', max_length=13),
        ),
        migrations.AlterField(
            model_name='paywithbank',
            name='transaction_no',
            field=models.CharField(max_length=100),
        ),
    ]
