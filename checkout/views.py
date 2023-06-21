from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # gets the current session bag 
    bag = request.session.get('bag', {})

    # Stops users from manually accessing the URL my typing it in
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)