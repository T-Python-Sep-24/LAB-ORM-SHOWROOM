from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from cars.models import Car, Color
from brands.models import Brand
# Create your views here.

def home_view(request: HttpRequest):
    featured_cars = Car.objects.all()[:4]
    featured_brands = Brand.objects.all()[:4]
    return render(request, 'index.html', context={'cars': featured_cars, 'brands':featured_brands})

def search_view(request: HttpRequest):

    if 'keyword' in request.GET and len(request.GET['keyword']) >= 3:
        keyword = request.GET['keyword']

        car_results = Car.objects.filter(
            Q(name__contains=keyword) |
            Q(specs__contains=keyword) |
            Q(model_year__contains=keyword)
        )
        brand_results = Brand.objects.filter(
            Q(name__contains=keyword) |
            Q(about__contains=keyword) |
            Q(founded_at__contains=keyword)
        )

    else:
        car_results = []
        brand_results = []

    return render(request, 'search_results.html', context={'cars': car_results, 'brands': brand_results})
