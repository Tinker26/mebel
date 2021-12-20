
from django.urls import path,include
from .views import *

# from habibi.views import *
urlpatterns = [

    path('', grid, name="grid"),
    path('<slug:category_slug>/', grid , name="grid_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/', product_info, name="product_info"),
] 
