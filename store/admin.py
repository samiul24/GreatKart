from django.contrib import admin
from . models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    list_display        = ['id', 'name', 'slug', 'stock', 'price', 'images', 'is_available', 'category']
    list_display_links  = ('id', 'name',)
    list_filter         = ['name']
    search_fields       = ['name']
    ordering            = ['id']

admin.site.register(Product, ProductAdmin)
