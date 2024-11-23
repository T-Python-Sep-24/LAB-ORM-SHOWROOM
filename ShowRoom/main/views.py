from django.shortcuts import render
from django.http import HttpRequest
from cars.models import Car
from brands.models import Brand
from django.db.models import Count


# Create your views here.


def home_view(request):

     cars = Car.objects.all().order_by('-id')[:3]

     brands = Brand.objects.all()
     top_brand = max(brands, key=lambda brand: brand.get_car_count(), default=None)

 
     return render(request, 'main/home.html', {'cars': cars , 'top_brand':top_brand})