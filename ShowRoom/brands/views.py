from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Brand
from .forms import BrandForm

from cars.models import Car

from django.contrib import messages


def all_brands_view(request:HttpRequest):
    brands = Brand.objects.all()
    
    return render(request, "brands/all_brands.html", {'brands': brands})

def brand_detail_view(request:HttpRequest, brand_id:int):
    brand = Brand.objects.get(pk=brand_id)
    cars = Car.objects.filter(brand=brand)
    
    return render(request, "brands/brand_detail.html", {'brand': brand, 'cars': cars})


def new_brand_view(request:HttpRequest):
    brand_form = BrandForm()
    
    if request.method == "POST":
        brand_form = BrandForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, "Added Brand Successfuly!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", brand_form.errors)
            messages.error(request, "Couldn't Add Brand!", "alert-danger")
    
    return render(request, "brands/brand_add.html")

def search_brands_view(request:HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        brands = Brand.objects.filter(name__contains=request.GET["search"])
    
    else:
        brands = []
    
    return render(request, "brands/brand_search.html", {'brands': brands,})

    
    
    


    
    
    