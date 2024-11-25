from django.http import HttpRequest
from django.shortcuts import render
from cars.models import Car
from brands.models import Brand

def home(request: HttpRequest):
   all_cars = Car.objects.all()[:5]  
   all_brands = Brand.objects.all()[:5]
   return render(request, 'main/home.html', {
        'all_cars': all_cars,
        'all_brands': all_brands,
    })
def about(request: HttpRequest):
    return render(request, 'main/about.html')