from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home_view(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME,
        'restaurant_phone': settings.RESTAURANT_PHONE
    }
    return render(request,'index.html', context)

def about_view(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'about.html',context)

def menu_view(request):
    menu_items = [
        {'name':"Margherita Pizza", 'price': 'Rs. 150','description':'Classic pizza with tomato sauce and mozzarella.'},
        {'name':"Veggie Burger", 'price': 'Rs. 125','description':'Grilled veggie patty with letuce, tomato, and aioli.'},
        {'name':"Pasta Alfredo", 'price': 'Rs. 200','description':'Creamy Alfredo sauce over fettuccine pasta.'},
        {'name':"Caesar salad", 'price': 'Rs. 100','description':'Fresh romaine lettuce with Caesar dressing and croutons.'},
    ]
    return render(request,'menu.html',{"menu_items": menu_items})