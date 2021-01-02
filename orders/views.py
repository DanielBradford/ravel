from django.shortcuts import render, redirect
from django import template
import string
import random

# from .models import Product, Color, Size

# register = template.Library()

# @register.filter
# def get_type(value):
#     return type(value)


# # # Create your views here.
# products = Product.objects.all()
# colors = Color.objects.all()
# size = Size.objects.all()

# context = {
#     'products': products,
#     'colors': colors,
#     'size': size
# }

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def orders(request):
    """ A view to render the orders page"""
    return render(request, 'orders/orderForm.html')


def add_to_order(request, item_id):
                
    """ Add a quantity of the specified product to the order """
    orderID = id_generator()
    quantity = float(request.POST.get('quantity'))
    color = str(request.POST.get('color'))
    size = str(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})
    order[item_id] = quantity, color, size, orderID
    request.session['order'] = order
    print(order)
    print(len(order))
    

    return redirect(redirect_url)


def delete_all_orders(request):
    redirect_url = request.POST.get('redirect_url')
    del request.session
    return redirect(redirect_url)

