from .models import Product
from store.models import Category
from django.shortcuts import render, get_object_or_404

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        total_products = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        total_products = products.count()

    context = {
        'products': products,
        'total_products': total_products,

    }

    return render(request, 'store/store.html', context)

def product_detail(request,category_slug, product_slug):
    return render(request, 'store/product_detail.html')