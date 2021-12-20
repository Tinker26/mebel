"""habibi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
from store.views import *
from grid.views import *


from habibi.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('grid/',include('grid.urls')),
    path('store/',include('store.urls')),
    path('cart/', include('cart.urls')),
    path('grid2/', grid2, name="grid2"),
    path('product_info', product_info, name="product_info"),
    path('store2/', store2, name="store2"),
    path('store2/<slug:category_slug>/', store2, name="products2_by_category"),
    path('<slug:category_slug>/', Home, name="home_by_category"),
    path('grid2/<slug:category_slug>/',grid2, name="grid_by_category2"),
    path('product_info/<slug:category_slug>/',product_info, name="product_info"),
    
] + static(MEDIA_URL, document_root=MEDIA_ROOT)