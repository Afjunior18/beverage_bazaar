from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """
    Render the shopping bag page.
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a specified quantity of a product to the shopping bag.
    """

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/products/')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added "{product.name}" to your bag!')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
