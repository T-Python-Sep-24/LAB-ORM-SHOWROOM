from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q, Count
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from cars.models import Car, Color
from brands.models import Brand
from .forms import TestDriveRequestForm
# Create your views here.


def home_view(request: HttpRequest):
    featured_cars = Car.objects.all()[:4]
    featured_brands = Brand.objects.annotate(car_count=Count('car'))[:4]
    return render(request, 'index.html', context={'cars': featured_cars, 'brands':featured_brands})


def search_view(request: HttpRequest):

    if 'keyword' in request.GET and len(request.GET['keyword']) >= 3:
        keyword = request.GET['keyword']

        car_results = Car.objects.filter(
            Q(name__contains=keyword) |
            Q(specs__contains=keyword) |
            Q(model_year__contains=keyword)
        )
        featured_brands = Brand.objects.annotate(car_count=Count('car'))
        # brand_results = Brand.objects.filter(
        #     Q(name__contains=keyword) |
        #     Q(about__contains=keyword) |
        #     Q(founded_at__contains=keyword)
        # )
        brand_results = featured_brands.filter(
                    Q(name__contains=keyword) |
                    Q(about__contains=keyword) |
                    Q(founded_at__contains=keyword)
                )

    else:
        car_results = []
        brand_results = []

    return render(request, 'search_results.html', context={'cars': car_results, 'brands': brand_results})


def test_drive_view(request: HttpRequest):

    brands = Brand.objects.all()
    cars = Car.objects.all()
    if request.method == "POST":
        test_drive_request_form = TestDriveRequestForm(request.POST)
        if test_drive_request_form.is_valid():
            test_drive_request_form.save()
            messages.success(request, 'Your request was sent successfully', 'alert-success')
        else:
            messages.error(request, 'Error Processing your request', 'alert-danger')
    return render(request, 'test_drive.html', context={'cars': cars, 'brands': brands})
