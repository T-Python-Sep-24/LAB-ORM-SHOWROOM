from django.shortcuts import render,redirect
from django.http import HttpRequest , HttpResponse

def all_brands_view(request:HttpRequest):
  
    return render(request, 'brands_app/all_brands.html')

def brand_detail_view(request:HttpRequest,):
    
    return render(request, 'brands_app/brand_detail.html')

def new_brand_view(request:HttpRequest):
  
    return render(request, 'brands_app/add_new_brand.html')

def update_brand_view(request:HttpRequest):

    return render(request, 'brands_app/update_brand.html')
# Create your views here.
