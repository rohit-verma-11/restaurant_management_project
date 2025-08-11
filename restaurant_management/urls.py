from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import custom_page_not_found
from django.conf.urls import handler404

handler404 = custom_page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls') , name="home"),
    path('api/' , include('home.urls') , name='api'),
    path('api/accounts/' , include('account.urls') , name='api_accounts'),
    path('api/products/' , include('products.urls') , name='api_products'),
    path('api/orders/' , include('orders.urls') , name='api_urls'),
]
