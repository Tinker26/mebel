from django.contrib import admin
from .models import *


class CartitemAdmin(admin.ModelAdmin):
    list_display= ('product','cart','quantity', )
    list_display_link = ('product',)
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display= ('date_added','session_id' )
    list_display_link = ('session_id',)
# Register your models here.

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartitemAdmin)