from django.shortcuts import render
from cars.models import Car
from brands.models import Brand

def home(request):
    latest_cars = Car.objects.all().order_by('-id')[:4]
    latest_brands = Brand.objects.all().order_by('-id')[:4]
    return render(request, 'main/home.html', {'latest_cars': latest_cars, 'latest_brands': latest_brands})
