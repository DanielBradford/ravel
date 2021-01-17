from django.shortcuts import render, redirect, reverse, HttpResponse
from django import template
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def orders(request):
    """ A view to render the orders page"""
    return render(request, 'orders/orderList.html')


def add_to_order(request, item_id):
                
    """ Add a quantity of the specified product to the order """
    orderID = id_generator()
    quantity = int(request.POST.get('quantity'))
    color = str(request.POST.get('color'))
    size = str(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})
    print(order)
    order[item_id] = quantity, color, size, orderID
    request.session['order'] = order
    return redirect(redirect_url)

    # if item_id in list(order.keys()):
    #     order[orderID] = quantity, color, size, orderID, item_id
    #     request.session['order'] = order
    #     return redirect(redirect_url)
    #     # messages.success(request, f'Updated {product.name} quantity to {order[item_id]}')
    # else:
    #     order[item_id] = quantity, color, size, orderID
    #     request.session['order'] = order
    #     return redirect(redirect_url)
        # messages.success(request, f'Added {product.name} to your bag')
    # order[item_id] = quantity, color, size, orderID
    # request.session['order'] = order
    # return redirect(redirect_url)


# def update_order(request, order_id):
                
#     """ Update the quantity of the specified product to the order """
#     quantity = int(request.POST.get('quantity'))
#     order = request.session.get('order', {})
#     if quantity > 0:
#         for item in order.items:
#             if item.order_id == order_id:
#                 item.quantity = quantity
#     else:
#         order.pop(order_id)
#     request.session['order'] = order
#     return redirect(reverse('orders'))


def remove_from_order(request, item_id):
    order = request.session.get('order', {})
    print(order)
    # for item in order:
    #     if item.item_id == item_id:
    order.pop(item_id)
    request.session['order'] = order
    return HttpResponse(status=200)
        # else:
        #     request.session['order'] = order
        #     return HttpResponse(status=200)


def delete_session(request):
    if 'order' in request.session:
        del request.session['order']
    order = request.session.get('order', {})
    request.session['order'] = order
    return redirect(reverse('orders'))






   
  
