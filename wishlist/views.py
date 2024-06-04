from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Wishlist
from products.models import Product
from .forms import WishlistForm

# Create your views here.

def add_to_wishlist(request, product_id):
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
            return redirect('wishlist')
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    return redirect('wishlist')

def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    products = []
    for item in wishlist_items:
        products.extend(list(item.products.all()))
    return render(request, 'wishlist/wishlist.html', {'products': products})