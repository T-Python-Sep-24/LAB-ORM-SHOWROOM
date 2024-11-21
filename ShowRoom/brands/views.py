from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def all_brands(request):
    return render(request, 'brands/all_brands.html') 

def create_brand(request):
    return render(request, 'brands/create_brand.html') 

def brand_detail(request):
    return render(request, 'brands/brand_detail.html') 

def brand_update(request):
    return render(request, 'brands/brand_update.html') 

def brand_delete(request):
    return render(request, 'brands/brand_delete.html') 