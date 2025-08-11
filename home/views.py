from django.shortcuts import render
from django.conf import settings

# Create your views here.
def homepage(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'index.html', context)

def aboutpage(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'about.html',context)