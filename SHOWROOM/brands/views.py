from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse


# Create your views here.

def all_brands_view(request:HttpRequest):

    return render(request, 'brands/all_brands.html')




def add_new_brand_view(request:HttpRequest):

    return render(request, 'brands/add_new_brand.html')




def brand_details_view(request:HttpRequest):

    return render(request, 'brands/brand_details.html')




def brand_update_view(request:HttpRequest):

    return render(request, 'brands/update_brand.html')




def brand_delete_view(request:HttpRequest):

    return render(request, 'brands/brand_delete.html')

