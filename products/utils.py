def remove_item_from_bag(request, product):
    if 'bag' in request.session:
        bag = request.session['bag']
        if str(product.id) in bag:
            del bag[str(product.id)]
            request.session['bag'] = bag
    else:
        return None

    return True