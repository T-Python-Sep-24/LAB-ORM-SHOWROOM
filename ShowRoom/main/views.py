from django.shortcuts import render
from cars.models import Car
from brands.models import Brand

def index_view(request):
    latest_cars = Car.objects.all().order_by('-id')[:4]  # Fetch the latest 4 cars
    latest_brands = Brand.objects.all().order_by('-id')[:4]  # Fetch the latest 4 brands
    return render(request, 'main/index.html', {
        'latest_cars': latest_cars,
        'latest_brands': latest_brands,
    })


