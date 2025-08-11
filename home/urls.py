from django.urls import path
from .views import *

urlpatterns = [
    path('' , homepage , name='homepage')
    path('about/',about_page,name='about')
]