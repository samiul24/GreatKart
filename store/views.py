from django.core import paginator
from django.http.response import HttpResponse
from .models import Product
from store.models import Category
from carts.models import Cart, CartItem
from carts.views import _cart_id

from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        total_products = products.count()
        paginator = Paginator(products, 3)
        #print(paginator)
        page = request.GET.get('page')
        #print(page)
        paged_products = paginator.get_page(page)
        #print(paged_products)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        total_products = products.count()
        paginator = Paginator(products, 3)
        #print(paginator)
        page = request.GET.get('page')
        #print(page)
        paged_products = paginator.get_page(page)
        #print(paged_products)
        #print(paged_products.has_other_pages)

    context = {
        'products': paged_products,
        'total_products': total_products,

    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    #print(category_slug)
    #print(product_slug)
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        #in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product.id)
        #print(in_cart.query) /*Without exists() it works*/
        #print(in_cart)
        #print(single_product)
        #print(single_product.id)
    except Exception as e:
        raise e 
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }

    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(name__icontains=keyword)).order_by('-create_date')
            total_products = products.count()
    context = {
            'products': products,
            'total_products' : total_products,
        }
    return render(request, 'store/store.html', context)