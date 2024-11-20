from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from cars.models import Car, Color
from brands.models import Brand
# Create your views here.

def home_view(request: HttpRequest):
    featured_cars = Car.objects.all()[:4]
    featured_brands = Brand.objects.all()[:4]
    return render(request, 'index.html', context={'cars': featured_cars, 'brands':featured_brands})
