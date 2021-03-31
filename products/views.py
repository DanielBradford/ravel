from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Color, Size


def all_products(request):
    """ A view to show all products,
    including sorting and search queries """

    products = Product.objects.all()
    colors = Color.objects.all()
    size = Size.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            colors = Color.objects.all()
            size = Size.objects.all()

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            colors = Color.objects.all()
            size = Size.objects.all()

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, '''You didn't enter
                                            any search criteria!''')
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query)
                       )
            products = products.filter(queries)
            colors = Color.objects.all()
            size = Size.objects.all()

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'colors': colors,
        'size': size,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """A View to return product details"""

    product = get_object_or_404(Product, pk=product_id)
    colors = Color.objects.all()
    size = Size.objects.all()

    context = {
        'product': product,
        'colors': colors,
        'size': size
    }

    return render(request, 'products/product_detail.html', context)
