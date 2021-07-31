from django.db import models
from category.models import Category


class Product(models.Model):
    name        = models.CharField(max_length=200, unique=True)
    slug        = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    price       = models.FloatField()
    images      = models.ImageField(upload_to='photos/products')
    stock       = models.FloatField()
    is_available   = models.BooleanField(default=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
