from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def all_brands_view(request:HttpRequest):
    
    return render(request, "brands/.html")

def brand_detail_view(request:HttpRequest, brand_id:int):
    
    return render(request, "brands/.html")



def new_brand_view(request:HttpRequest):
    
    return render(request, "brands/.html")

def brand_update_view(request:HttpRequest, brand_id:int):
    
    return render(request, "brands/.html")

def brand_delete_view(request:HttpRequest,  brand_id:int):
    
    return render(request, "brands/.html")


    
    
    