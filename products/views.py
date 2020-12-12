from django.shortcuts import render
from .models import Product, Color, Size

# Create your views here.

products = Product.objects.all()
colors = Color.objects.all()
size = Size.objects.all()

context = {
    'products': products,
    'colors': colors,
    'size': size
}


def all_products(request):
    """ A view to return the all products page with option to search and sort"""
    return render(request, 'products/products.html', context)


def view_product(request):
    """A View to return product details"""
    return render(request, 'products/product_detail', context)