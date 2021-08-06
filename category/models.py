from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    description=models.TextField(max_length=1000, blank=True)
    image=models.ImageField(upload_to='photos/category', blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    
    def get_url(self):
        return reverse('store_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    
