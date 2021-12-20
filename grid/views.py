from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from category.models import Category
from .models import *
# Create your views here.
def grid(request, category_slug=None):
    if category_slug == None:
        products = Product_grid.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product_grid.objects.filter(is_available=True, category=categories)

    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'blog_grid.html', context)

def grid2(request, category_slug=None):
    if category_slug == None:
        products = Product_grid.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product_grid.objects.filter(is_available=True, category=categories)

    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'blog_list.html', context)

def product_info(request, category_slug=None):
    if category_slug == None:
        products = Product_grid.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product_grid.objects.filter(is_available=True, category=categories)

    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'blog_info.html', context)


