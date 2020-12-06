from django.shortcuts import render, redirect

# Create your views here.


def orders(request):
    """ A view to renders the orders page"""
    return render(request, 'orders/orderForm.html')


def add_to_order(request, item_id):
                
    """ Add a quantity of the specified product to the order """

    quantity = int(request.POST.get('quantity'))
    color = request.POST.get('color')
    size = request.POST.get('size')
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})

    if item_id in list(order.keys()):
        order[item_id] += quantity
    else:
        order[item_id] = quantity, color, size

    request.session['order'] = order
    print(request.session['order'])
    return redirect(redirect_url)
