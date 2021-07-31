from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


products=Product.objects.all()
context={
    'products':products,
}

def home(request):
    return render(request, 'home.html', context)