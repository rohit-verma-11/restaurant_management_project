from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'index.html', context)