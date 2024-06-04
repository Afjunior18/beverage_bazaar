# Generated by Django 3.2 on 2024-06-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('wishlist', '0002_auto_20240604_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product_id',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
