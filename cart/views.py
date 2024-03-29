from django.shortcuts import render , get_object_or_404, redirect
from store.models import Product
from .models import *
from django.core.exceptions import ObjectDoesNotExist

def cart(request):
    cart_items = None 
    try:
        cart = Cart.objects.get(session_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart)
        total = 0
        for cart_item in cart_items:
            total += cart_item.quantity * cart_item.product.price
       
    except ObjectDoesNotExist:
        pass
    context = {
        'cart_items': cart_items,
        'total': total,
       
    }
    return render(request, 'cart.html',context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):        
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))      
    except Cart.DoesNotExist:
        cart = Cart.objects.create(session_id=_cart_id(request))
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
    return redirect('cart')


def sub_cart(request, product_id):
    cart = Cart.objects.get(session_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:

        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(session_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')