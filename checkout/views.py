from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    # stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # stripe_secret_key = settings.STRIPE_SECRET_KEY
    # stripe.api_key = stripe_public_key
    # intent = stripe.PaymentIntent.create(
    # amount=stripe_total,
    # currency=settings.STRIPE_CURRENCY,
    # )
    # print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LoIlXHf0nhYIfPjiICCKh2RTzyZbxzpyEUqNH1ECG7M9zc6iwp7hOrwsH0BAFOZeYXSqDndo9GXUO9JwgRnURX300V1H0KpHq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
