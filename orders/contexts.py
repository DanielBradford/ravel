from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Color, Size


def order_contents(request):
    order_items = []
    total = 0
    product_count = 0
    order = request.session.get('order', {})

    for item_id, quantity in order.items():
        product = get_object_or_404(Product, pk=item_id)
        # color = get_object_or_404(Color, pk=item_id)
        # size = get_object_or_404(Size, pk=item_id)

        total = product.price
        print(total)
        product_count = quantity
        order_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

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