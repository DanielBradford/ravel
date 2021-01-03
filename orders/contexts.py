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
    colors = Color.objects.all()

    for item_id, orderData in order.items():
        product = get_object_or_404(Product, pk=item_id)
        print(orderData)
        colorChoice = orderData[1]
        print(colorChoice)
        for color in colors:
            if colorChoice == color.name:
                print("This is the color choice", colorChoice, color.cost)
                colorCost = color.cost
                sizeChoice = orderData[2]
                sizes = Size.objects.all()
                for size in sizes:
                    if sizeChoice == size.name:
                        sizeCost = decimal.Decimal(size.cost)
                        extras = decimal.Decimal(sizeCost + colorCost)
                        print("The extras are", extras)
                        total += (product.price + extras) * decimal.Decimal(orderData[0])
                        order_items.append({
                            'order_id': orderData[3],
                            'item_id': item_id,
                            'quantity': orderData[0],
                            'color': colorChoice,
                            'colorCost': colorCost,
                            'sizeCost': sizeCost,
                            'extras': extras,
                            'size': sizeChoice,
                            'product': product,
                            'this_total': (product.price + extras) * decimal.Decimal(orderData[0])
                        })
            else:
                colorCost = 0
        # print("TEST IF wrong", colorCost)
        # sizeChoice = quantity[2]
        # sizes = Size.objects.all()
        # for size in sizes:
        #     if sizeChoice == size.name:
        #         sizeCost = decimal.Decimal(size.cost)
            # else:
            #     sizeCost = 88
    
        # extras = decimal.Decimal(sizeCost + colorCost)
        # print("The extras are", extras)
        # total += (product.price + extras) * decimal.Decimal(quantity[0])
        # order_items.append({
        #     'item_id': item_id,
        #     'quantity': quantity[0],
        #     'color': colorChoice,
        #     'colorCost': colorCost,
        #     'sizeCost': sizeCost,
        #     'extras': extras,
        #     'size': sizeChoice,
        #     'product': product,
        #     'this_total': (product.price + extras) * decimal.Decimal(quantity[0])
        # })
                
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