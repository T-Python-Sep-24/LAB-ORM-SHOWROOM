from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Car, Color
from .forms import CarForm, ColorForm

from brands.models import Brand


def all_cars_view(request:HttpRequest):
    
    return render(request, "cars/all_cars.html")

def car_detail_view(request:HttpRequest, car_id:int):
    car = Car.objects.get(pk=car_id)
    
    return render(request, "cars/car_detail.html", {'car': car})



def new_car_view(request:HttpRequest):
    car_form = CarForm()
    
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect("main:home_view")
        else:
            print("not valid form", car_form.errors)
    
    return render(request, "cars/car_add.html", 
                           {
                            'categories': Car.Category.choices, 
                            'doors': Car.DoorChoices.choices, 
                            'colors': colors, 
                            'brands': brands
                            })

def car_update_view(request:HttpRequest, car_id:int):
    car = Car.objects.get(pk=car_id)
    
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    if request.method == "POST":
        car_form = CarForm(instance=car, data=request.POST, files=request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect("main:home_view")
        else:
            print("not valid form", car_form.errors)
            
        return redirect("cars:car_detail_view", car_id=car_id)
    
    return render(request, "cars/car_update.html", {
                            'car': car,
                            'categories': Car.Category.choices, 
                            'doors': Car.DoorChoices.choices, 
                            'colors': colors, 
                            'brands': brands
                            })

def car_delete_view(request:HttpRequest,  car_id:int):
    car = Car.objects.get(pk=car_id)
    car.delete()
    
    return redirect("main:home_view")



def new_color_view(request:HttpRequest):
    color_form = ColorForm()
    
    if request.method == "POST":
        color_form = ColorForm(request.POST)
        if color_form.is_valid():
            color_form.save()
            return redirect("main:home_view")
        else:
            print("not valid form", color_form.errors)
    
    return render(request, "cars/color_add.html")

def color_update_view(request:HttpRequest, color_id:int):
    
    return render(request, "cars/.html")

def color_delete_view(request:HttpRequest,  color_id:int):
    
    return redirect("main:home_view")


def search_cars_view(request:HttpRequest, color_id:int):
    
    return render(request, "cars/.html")

    
    
    