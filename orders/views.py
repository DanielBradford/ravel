from django.shortcuts import render, redirect, reverse, HttpResponse
from django import template
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def orders(request):
    """ A view to render the orders page"""
    return render(request, 'orders/orderForm.html')


def add_to_order(request, item_id):
                
    """ Add a quantity of the specified product to the order """
    orderID = id_generator()
    quantity = int(request.POST.get('quantity'))
    color = str(request.POST.get('color'))
    size = str(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})
    order[item_id] = quantity, color, size, orderID
    request.session['order'] = order
    print(order)
    print(len(order))
    return redirect(redirect_url)


def update_order(request, order_id):
                
    """ Update the quantity of the specified product to the order """
    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order', {})
    if quantity > 0:
        for item in order.items:
            if item.order_id == order_id:
                item.quantity = quantity
    else:
        order.pop(order_id)
    request.session['order'] = order
    return redirect(reverse('orders'))


def remove_from_order(request, order_id):
    order = request.session.get('order', {})
    for item in order.items:
        if item.order_id == order_id:
            order.pop(order_id)
            request.session['order'] = order
            return HttpResponse(status=200)
        else:
            request.session['order'] = order
            return HttpResponse(status=200)




   
  
