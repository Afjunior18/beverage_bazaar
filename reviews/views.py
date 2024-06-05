from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import Review

def product_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'reviews/product_review.html', context)