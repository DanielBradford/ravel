from django.shortcuts import render
from .models import Product

# Create your views here.

products = Product.objects.all()

context = {
    'products': products,
}

def all_products(request):
    """ A view to return the all products page with option to search and sort"""
    return render(request, 'products/products.html', context)