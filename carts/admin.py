from django.contrib import admin
from django.db import models
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display=['cart_id', 'date_added']

class CartItemAdmin(admin.ModelAdmin):
    list_display=['product', 'cart', 'quantity']

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)