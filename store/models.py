from django.db import models
from django.db.models.deletion import CASCADE
from category.models import Category
from django.urls import reverse

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

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug ])

    def __str__(self):
        return self.name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)
    

variation_category_choice=(
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active   = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    object = VariationManager()

    def __str__(self):
        return self.variation_value

    
