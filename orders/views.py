from django.shortcuts import render, redirect
# from .models import Product, Color, Size

# # Create your views here.
# products = Product.objects.all()
# colors = Color.objects.all()
# size = Size.objects.all()

# context = {
#     'products': products,
#     'colors': colors,
#     'size': size
# }


def orders(request):
    """ A view to render the orders page"""
    return render(request, 'orders/orderForm.html')


def add_to_order(request, item_id):
                
    """ Add a quantity of the specified product to the order """

    quantity = request.POST.get('quantity')
    color = str(request.POST.get('color'))
    size = str(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})

    if item_id in list(order.keys()):
        order[item_id] += quantity
    else:
        order[item_id] = quantity, color, size

    request.session['order'] = order
    print(order)
    print(len(order))
    # values = order.values()
    # totalof = sum(values)
    # print(totalof)

    return redirect(redirect_url)
