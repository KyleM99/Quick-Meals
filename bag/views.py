from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ Renders bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Quantity to shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shopping cart')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust Quantity """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
