from django.shortcuts import render, redirect

# Create your views here.


def orders(request):
    """ A view to renders the orders page"""
    return render(request, 'orders/orders.html')
