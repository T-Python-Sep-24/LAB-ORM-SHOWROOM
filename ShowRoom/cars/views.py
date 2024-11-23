from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Car , Color
from brands.models import Brand
# Create your views here.


def add_car_view(request:HttpRequest):
    if request.method == "POST":
        new_car = Car(
            name=request.POST["name"],
            brand=request.POST["brand"],
            photo=request.FILES["photo"],
            colors=request.POST["colors"],
            model_year=request.POST["model_year"],  
            price=request.POST["price"],
            fuel_type=request.POST["fuel_type"],
        )
        
        new_car.save()
        
        return redirect("cars:all_cars_view")  

    return render(request, "cars/add_car.html")

def all_cars_view(request:HttpRequest):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    return render(request,"cars/all_cars.html",{"cars":cars,"brands":brands,"colors":colors})


def detail_view(request:HttpRequest, car_id:int):
    return render(request,"cars/all_cars.html")

def update_view(request:HttpRequest, car_id:int):
    return render(request,"cars/all_cars.html")

def delete_view(request:HttpRequest, car_id:int):
    return render(request,"cars/all_cars.html")



def add_color(request:HttpRequest):
    if request.method == "POST":
        new_color = Color(
            name=request.POST["name"],
            photo=request.FILES["photo"],
            )
        new_color.save()
        
        return redirect("cars:all_cars_view") 
    return render(request,"cars/add_color.html")


def update_color(request:HttpRequest):
    return render(request,"cars/update_color.html")
