from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
    list_filter=['id', 'name']
    search_fields = ['name']
    ordering = ['id'] 

admin.site.register(Category,CategoryAdmin)

