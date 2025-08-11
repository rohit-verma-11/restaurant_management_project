from django.urls import path
from home.views import home_view, about_view, menu_view

urlpatterns = [
    path('', home_view , name='home'),
    path('about/', about_view, name='about'),
    path('menu/', menu_view, name='menu')
]