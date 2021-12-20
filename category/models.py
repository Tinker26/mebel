from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icons = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    # descriptions = models.TextField(blank=True)
    # image = models.ImageField(upload_to='photo/category',blank=True)

    def __str__(self) ->str:
        return self.name

    def get_home_url(self):
        return reverse('home_by_category', args=[self.slug])

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def get_urls(self):
        return reverse('products2_by_category',args=[self.slug])
    
    def get_grid_url(self):
          return reverse('grid_by_category',args=[self.slug])
    
    def get_list_url(self):
        return reverse('grid_by_category2',args=[self.slug])

