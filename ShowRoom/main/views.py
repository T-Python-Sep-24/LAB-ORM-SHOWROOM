from django.shortcuts import render, get_object_or_404
from cars.models import Car
from brands.models import Brand
# Create your views here.



def home(request):
    latest_cars = Car.objects.order_by('-id')[:4]
    latest_brands = Brand.objects.order_by('-id')[:4]
    return render(request, 'home.html', {'latest_cars': latest_cars,'latest_brands': latest_brands,})