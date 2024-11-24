from django.shortcuts import render , redirect 
from django.http import HttpRequest , HttpResponse
from cars_app.models import Car , Color
from brands_app.models import Brand
# Create your views here.

def home_view(request:HttpRequest):
    
    brands = Brand.objects.all()
    latest_cars = Car.objects.order_by('-id')[:4]  # Adjust as needed

    return render(request, 'main_app/home.html', {
        'brands': brands,
        'latest_cars': latest_cars,
    })
    # return render(request, 'main_app/home.html', {'brands': brands})

    # return render(request, "main_app/home.html")
