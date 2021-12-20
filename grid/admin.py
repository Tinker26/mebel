from django.contrib import admin
from .models import *

class Product_GridAdmin(admin.ModelAdmin):
    list_display= ('name', 'image', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
admin.site.register(Product_grid, Product_GridAdmin)