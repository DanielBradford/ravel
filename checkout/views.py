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
    }

    return render(request, template, context)