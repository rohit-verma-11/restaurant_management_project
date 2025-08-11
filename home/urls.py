from django.urls import path
from home.views import homepage, about_page, menu_view

urlpatterns = [
    path('' , homepage , name='homepage'),
    path('about/',about_page,name='about'),
    path('menu/',menu_view,name='menu'),
]