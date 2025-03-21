# Generated by Django 5.0.1 on 2024-04-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankpay', '0002_paywithbank_user_bank_account_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='paywithbank',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
