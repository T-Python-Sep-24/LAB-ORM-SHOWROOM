from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def all_cars_view(request:HttpRequest):
    
    return render(request, "cars/.html")

def car_detail_view(request:HttpRequest, car_id:int):
    
    return render(request, "cars/.html")



def new_car_view(request:HttpRequest):
    
    return render(request, "cars/.html")

def car_update_view(request:HttpRequest, car_id:int):
    
    return render(request, "cars/.html")

def car_delete_view(request:HttpRequest,  car_id:int):
    
    return render(request, "cars/.html")



def new_color_view(request:HttpRequest):
    
    return render(request, "cars/.html")

def color_update_view(request:HttpRequest, color_id:int):
    
    return render(request, "cars/.html")

def color_delete_view(request:HttpRequest,  color_id:int):
    
    return render(request, "cars/.html")



def search_cars_view(request:HttpRequest, color_id:int):
    
    return render(request, "cars/.html")

    
    
    