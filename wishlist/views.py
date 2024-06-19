from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http import HttpResponseBadRequest
from .models import Wishlist
from products.models import Product
from .forms import WishlistForm
from django.contrib import messages

from products.views import calculate_product_rating

# Create your views here.


def add_to_wishlist(request, product_id):
    """
    View to add a product to the user's wishlist.
    If the request is POST and the form is valid,
    the product is added to the wishlist.
    If the wishlist does not exist for the user, it is created.
    Success message is displayed upon successful addition.
    """

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Product, id=product_id)
            wishlist = Wishlist.objects.filter(user=request.user).first()
            if not wishlist:
                wishlist = Wishlist.objects.create(user=request.user)
            wishlist.products.add(product)
            wishlist_form = form.save(commit=False)
            wishlist_form.user = request.user
            wishlist_form.save()
            messages.success(request, "Added to your Wishlist!")
            return redirect('wishlist')
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def remove_from_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        wishlist = Wishlist.objects.filter(user=request.user).first()
        if wishlist:
            wishlist.products.remove(product)
        return redirect('wishlist')
    else:
        return HttpResponseBadRequest("Only POST requests are allowed")


def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    products = []
    for item in wishlist_items:
        products.extend(list(item.products.all()))

    # Calculating product rating for each product
    for product in products:
        product.rating = calculate_product_rating(product)

    return render(request, 'wishlist/wishlist.html', {'products': products})
