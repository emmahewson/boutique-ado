from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # puts the bag contents in to the session
    # checks if the bag already exists and if not creates it
    # as a python dictionary
    # the dictionary looks like
    # {'id': 'quantity'}
    bag = request.session.get('bag', {})

    # checks if a product has a size field
    if size:
        # handles products with a size field
        # if the same item in different sizes splits to separate items in bag
        # creates a dictionary within the dictionary
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # if no size on prodcut
        # checks if the item is already in the bag
        # uses the item id key from dictionary
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
