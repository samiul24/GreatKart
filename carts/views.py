from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from carts.models import CartItem, Cart
from store.models import Product

from django.http import HttpResponse


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    if request.method == 'POST':
        """return HttpResponse(request.POST['color'])
        exit()"""
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
    #return HttpResponse(cart_item.product)
    #exit()
    return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    #product = get_object_or_404(Product, id=product_id)
    #cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item = CartItem.objects.get(cart=cart, product=product_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    #product = get_object_or_404(Product, id=product_id)
    #cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item = CartItem.objects.get(cart=cart, product=product_id)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        #print(cart.id)
        #print(cart.cart_id)
        #print(cart.date_added)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        #print(cart_items.query)
        for cart_item in cart_items:
            total += (cart_item.product.price*cart_item.quantity)
            quantity += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
    }

    return render(request, 'store/cart.html', context)


