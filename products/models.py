from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Category(models.Model):
    type_product = models.CharField(max_length=254)

    def __str__(self):
        return self.type_product
    

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    region = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sku = models.CharField(max_length=50, unique=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.name
