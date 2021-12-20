from django.http import HttpResponse
from django.shortcuts import render
from django.http import request
from store.models import Product
from django.shortcuts import get_object_or_404, render
from category.models import Category
from grid.models import *
def Home(request, category_slug=None):
    if category_slug == None:
        products = Product.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)

    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'home.html', context)

