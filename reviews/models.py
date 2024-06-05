from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
    review_comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review {self.pk} by {self.user.username}'
