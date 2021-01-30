import decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Color, Size
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def order_contents(request):
    order_items = []
    total = 0
    product_count = 0
    order = request.session.get('order', {})

    for item_info, quantity in order.items():
        item_id, color_id, size_id = [int(value) for value in item_info.split()]
        product = get_object_or_404(Product, pk=item_id)
        color = get_object_or_404(Color, pk=color_id)
        size = get_object_or_404(Size, pk=size_id)
        colorCost = decimal.Decimal(color.cost)
        sizeCost = decimal.Decimal(size.cost)
        extras = sizeCost + colorCost
        quantity = quantity
        total += decimal.Decimal(float(product.price + extras) * float(quantity))
        order_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'color': color.name,
                        'colorCost': colorCost,
                        'sizeCost': sizeCost,
                        'extras': extras,
                        'size': size.name,
                        'product': product,
                        'this_total': float(product.price + extras) * int(quantity),
                        })

    # for item_id, orderData in order.items():
    #     product = get_object_or_404(Product, pk=item_id)
    #     colorChoice = orderData[1]
    #     for color in colors:
    #         if colorChoice == color.name:
    #             print("This is the color choice", colorChoice, color.cost)
    #             colorCost = color.cost
    #             sizeChoice = orderData[2]
    #             sizes = Size.objects.all()
    #             for size in sizes:
    #                 if sizeChoice == size.name:
    #                     sizeCost = decimal.Decimal(size.cost)
    #                     extras = decimal.Decimal(sizeCost + colorCost)
    #                     print("The extras are", extras)
    #                     total += (product.price + extras) * decimal.Decimal(orderData[0])
    #                     order_items.append({
    #                         'order_id': orderData[3],
    #                         'item_id': item_id,
    #                         'quantity': orderData[0],
    #                         'color': colorChoice,
    #                         'colorCost': colorCost,
    #                         'sizeCost': sizeCost,
    #                         'extras': extras,
    #                         'size': sizeChoice,
    #                         'product': product,
    #                         'this_total': (product.price + extras) * decimal.Decimal(orderData[0])
    #                     })
    #         else:
    #             colorCost = 0
                
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = total + delivery

    context = {

        'order_items': order_items,
        'total':  total,
        'product_count':  product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context