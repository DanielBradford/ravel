from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    order = request.session.get('order', {})
    if not order:
        messages.error(request, "There's nothing in your order at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = { 
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HaMScH8WfdiqwToKUMAMbY3QaTTOTHWwFHvbq5iq6CNKFMmeJ6oQqoiknQCIwddRu7TVRrGK4abMQmTQW9YO4yp00vAXCT6uz',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)