from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from .models import Product, Category

from reviews.forms import ReviewForm


# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None
    region = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
        
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            
            products = products.order_by(sortkey)


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
    
    current_sorting = f'{sort}_{direction}'

    # Calculating product rating for each product
    for product in products:
        product.rating = calculate_product_rating(product)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_region': region,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    # calculate avarage rating
    product_rating = calculate_product_rating(product)

    context = {
        'product': product,
        'form': form,
        'product_rating': product_rating,
    }

    return render(request, 'products/product_detail.html', context)


def calculate_product_rating(product):
    rating_avg = product.reviews.aggregate(Avg('rating'))['rating__avg']
    return rating_avg if rating_avg is not None else 0