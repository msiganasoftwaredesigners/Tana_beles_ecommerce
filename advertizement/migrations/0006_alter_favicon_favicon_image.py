# Generated by Django 5.0.1 on 2024-04-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertizement', '0005_alter_advertizementfirst_advertizement_first_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favicon',
            name='favicon_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/favicon'),
        ),
    ]
