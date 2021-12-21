from django.http import HttpResponse
from django.shortcuts import render
from django.http import request
from store.models import Product
from django.shortcuts import get_object_or_404, render
from category.models import Category
from grid.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def Home(request, category_slug=None):
    if category_slug == None:
        products = Product.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)

    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products': paged_products,
        'product_count': products.count()
    }
    return render(request, 'home.html', context)

