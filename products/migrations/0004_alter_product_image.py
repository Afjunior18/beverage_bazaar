# Generated by Django 3.2 on 2024-06-18 16:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
