import requests
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import BrandForm
from .models import Brand
from cars.models import Car
# Create your views here.

def all_brands_view(request: HttpRequest):

    brands = Brand.objects.annotate(car_count=Count('car'))
    paginator = Paginator(brands, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "GET":
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']

            brands = Brand.objects.filter(
                Q(name__contains=keyword) |
                Q(about__contains=keyword) |
                Q(founded_at__contains=keyword)
            )

    return render(request, 'all_brands.html', context={'brands': brands, 'page_obj': page_obj})


def brand_details_view(request: HttpRequest, brand_id:int):

    brand = Brand.objects.get(pk=brand_id)
    cars = Car.objects.filter(brand = brand)

    return render(request, 'brand_details.html', context={'brand':brand, 'cars': cars})


def add_brand_view(request: HttpRequest):

    try:
        if request.method == "POST":
            brand_form = BrandForm(request.POST, request.FILES)
            if brand_form.is_valid():
                brand_form.save()
                messages.success(request, "Brand was Added successfully", "alert-success")

                # if request.path == '/'
                return redirect('brands:all_brands_view')
            else:
                print("brand form is not valid")
                messages.error(request, "Error in adding this brand", "alert-danger")
        return render(request, 'add_brand.html')
    except Exception as e:
        print(e)


def update_brand_view(request:HttpRequest, brand_id: int):

    brand = Brand.objects.get(pk=brand_id)

    if request.method == "POST":
        brand_form = BrandForm(request.POST, request.FILES, instance=brand)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, "Brand was updated successfully", "alert-success")
            return redirect("brands:brand_details_view", brand_id=brand_id)
        else:
            print("Brand update Form is not valid")
            messages.error(request, "Error in Updating this brand", "alert-danger")
    return render(request, 'update_brand.html', context={'brand': brand})


def delete_brand_view(request:HttpRequest, brand_id):

    try:
        brand = Brand.objects.get(pk=brand_id)
        brand.delete()
        messages.success(request, "Brand was deleted Successfully", "alert-success")
        return redirect('brands:all_brands_view')
    except Exception as e:
        print(e)