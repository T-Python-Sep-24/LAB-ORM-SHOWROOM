from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Brand
from .forms import BrandForm
from django.contrib import messages
from django.db.models import ProtectedError



# Create your views here.

def all_brands(request: HttpRequest):
    brands = Brand.objects.all()  
    return render(request, "brands/all_brands.html", {"brands": brands})


def brand_detail(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(id=brand_id) 
    return render(request, "brands/brand_detail.html", {"brand": brand})


def new_brand(request: HttpRequest):
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('brands:all_brands')  
    else:
        form = BrandForm()

    return render(request, "brands/new_brand.html", {"form": form})

def update_brand(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(id=brand_id)  
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES, instance=brand)  
        if form.is_valid():
            form.save()  
            return redirect('brands:brand_detail', brand_id=brand.id)  
    else:
        form = BrandForm(instance=brand)

    return render(request, "brands/update_brand.html", {"form": form, "brand": brand})

def delete_brand(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(id=brand_id)
    try:
        brand.delete()
        messages.success(request, f"{brand.name} deleted successfully.")
    except ProtectedError:
        messages.error(request, f"Cannot delete {brand.name}, as it is associated with cars.")
    
    return redirect('brands:all_brands')
