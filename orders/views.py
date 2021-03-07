from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product, Color, Size
from django import template
import string
import random



def id_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def orders(request):
    """ A view to render the orders page"""
    return render(request, 'orders/orderList.html')


def add_to_order(request, item_id):
                
    """ Add a quantity of the specified product to the order """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    color = str(request.POST.get('color'))
    size = str(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})
    newItemID = str(item_id)
    order_info = newItemID + " " + color + " " + size
    if order_info in list(order.keys()):
        order[order_info] += quantity
        messages.success(request, f'Updated {product.name} quantity')

    else:
        order[order_info] = quantity
        messages.success(request, f'Added {quantity} x {product.name} to your basket')
    print(order)
    request.session['order'] = order
    return redirect(redirect_url)


def update_order(request):   
    """ Update the quantity of the specified product to the order """
    order = request.session.get('order', {})
    quantity = int(request.POST.get('quantity'))
    sizeID = str(request.POST.get('sizeID'))
    colorID = str(request.POST.get('colorID'))
    productID = str(request.POST.get('productID'))
    order_item_identifier = productID + " " + colorID + " " + sizeID
    if quantity > 0:
        order[order_item_identifier] = quantity
        print(str(order_item_identifier))
    else:
        order.pop(order_item_identifier)
    request.session['order'] = order
    return redirect(reverse('orders'))

    # except:
    #     redirect_url = request.POST.get('redirect_url')
    #     request.session['order'] = order
    #     return redirect(redirect_url)
    
def remove_from_order(request):
    """Remove the item from the shopping basket"""
    try:
        order = request.session.get('order', {})
        sizeID = str(request.POST.get('sizeID'))
        colorID = str(request.POST.get('colorID'))
        productID = str(request.POST.get('productID'))
        order_item_identifier = productID + " " + colorID + " " + sizeID

        # order[order_item_identifier] = int(request.post.get('quantity'))
        print(str(order_item_identifier))
        redirect_url = request.POST.get('redirect_url')
        order.pop(str(order_item_identifier))
        request.session['order'] = order
        return redirect(redirect_url)
    except Exception as e:
        redirect_url = request.POST.get('redirect_url')
        return redirect(redirect_url)


def delete_session(request):
    if 'order' in request.session:
        del request.session['order']
    order = request.session.get('order', {})
    request.session['order'] = order
    return redirect(reverse('orders'))






   
  
