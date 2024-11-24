from django.shortcuts import render , redirect 
from django.http import HttpRequest , HttpResponse
from cars_app.models import Car , Color
from brands_app.models import Brand
# Create your views here.

def home_view(request:HttpRequest):
    
    brands = Brand.objects.order_by('-id')[:5]
    # latest_cars = Car.objects.order_by('-id')[:4]  # Adjust as needed
    cars = Car.objects.all()

    return render(request, 'main_app/home.html', {
        'brands': brands,
        'cars': cars,
    })
    # return render(request, 'main_app/home.html', {'brands': brands})

    # return render(request, "main_app/home.html")
