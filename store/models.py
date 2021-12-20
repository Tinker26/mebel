from django.db import models    
from category.models import *
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    # description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    old_price = models.IntegerField()
    image = models.ImageField(upload_to = 'photoes/products')
    brand_name = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    description = models.TextField()
    # stock ombordegi soni
    stock = models.IntegerField(default=100)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])
