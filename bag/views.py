from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # puts the bag contents in to the session
    # checks if the bag already exists and if not creates it
    # as a python dictionary
    # the dictionary looks like
    # {'id': 'quantity'}
    bag = request.session.get('bag', {})

    # checks if the item is already in the bag
    # uses the item id key from dictionary
    if item_id in list(bag.keys()):
        # if so increments it by the chosen quantity
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
