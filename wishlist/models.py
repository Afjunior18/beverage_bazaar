from django.contrib.auth.models import User
from django.db import models

from products.models import Product, Category

# Create your models here.

class Wishlist(models.Model):
    """
    Model representing a Wishlist.
    Each wishlist belongs to a single user and can contain multiple products.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username}'s wishlist"
