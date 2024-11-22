from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Brand
from .forms import BrandForm


def all_brands_view(request:HttpRequest):
    
    return render(request, "brands/all_brands.html")

def brand_detail_view(request:HttpRequest, brand_id:int):
    
    return render(request, "brands/brand_detail.html")



def new_brand_view(request:HttpRequest):
    brand_form = BrandForm()
    
    if request.method == "POST":
        brand_form = BrandForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            return redirect("main:home_view")
        else:
            print("not valid form", brand_form.errors)
    
    return render(request, "brands/brand_add.html")

def brand_update_view(request:HttpRequest, brand_id:int):
    
    return render(request, "brands/brand_update.html")

def brand_delete_view(request:HttpRequest,  brand_id:int):
    
    return redirect("main:home_view")


    
    
    