# Generated by Django 5.0.1 on 2024-02-29 03:25

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
