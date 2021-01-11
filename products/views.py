from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Color, Size

# Create your views here.

products = Product.objects.all()
colors = Color.objects.all()
size = Size.objects.all()

context = {
    'products': products,
    'colors': colors,
    'size': size,
}


def all_products(request):
    """ A view to return the all products page with option to search and sort"""
    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """A View to return product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'colors': colors,
        'size': size
    }

    return render(request, 'products/product_detail.html', context)