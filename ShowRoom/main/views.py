from django.http import HttpRequest
from django.shortcuts import render
from cars.models import Car
from brands.models import Brand

def home(request: HttpRequest):
    latest_cars = Car.objects.order_by('-id')[:10]  
    latest_brands = Brand.objects.order_by('-id')[:4]  
    return render(request, 'main/home.html', {
        'latest_cars': latest_cars,
        'latest_brands': latest_brands,
    })
