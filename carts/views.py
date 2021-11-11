from django.shortcuts import redirect, render
from carts.models import CartItem, Cart
from store.models import Product

from django.http import HttpResponse

def cart(request):
    return render(request, 'store/cart.html')

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
            )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product, 
            cart = cart,
            quantity = 1,
        )
        cart_item.save()
    #print(type(cart_item))
    return HttpResponse(cart_item.product)
    exit()

    return redirect('cart')


