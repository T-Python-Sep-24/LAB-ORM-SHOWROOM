from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Brand
from django.contrib import messages

def all_brands_view(request:HttpRequest):
    brands = Brand.objects.all()
    return render(request, "brand/brand.html", {'brands': brands})

def brand_detail_view(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, "brand/detail_brand.html", {"brand": brand})

def add_brand_view(request:HttpRequest):
    if request.method == "POST":
        name = request.POST["name"]
        logo = request.FILES["logo"]
        about = request.POST["about"]
     
        Brand.objects.create(name=name, logo=logo, about=about)
        messages.success(request, "Brand added successfully!")
        return redirect("main:home_view")
    return render(request, "brand/add_brand.html")

def update_brand_view(request:HttpRequest, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        brand.name = request.POST["name"]
        brand.logo = request.FILES["logo"]
        brand.about = request.POST["about"]
        brand.save()
        messages.success(request, "Brand updated successfully!")
        return redirect("brands:all_brand_view")
    return render(request, "brand/brand_update.html", {"brand": brand})


def delete_brand_view(request:HttpRequest,brand_id):
      
      brand = Brand.objects.get(pk=brand_id)
      brand.delete()
      return redirect("main:home_view")