from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None
    region = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__type_product__in=categories)
            categories = Category.objects.filter(type_product__in=categories)
        
        if 'region' in request.GET:
            region = request.GET['region']
            if region and region != 'All':
                products = products.filter(region__iexact=region)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_region': region,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show a a specific product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
