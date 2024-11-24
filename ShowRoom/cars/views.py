from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Car, Color
from brands.models import Brand
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib import messages

def all_cars_view(request:HttpRequest):
    cars = Car.objects.all()
    paginator = Paginator(cars, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "main/all_cars.html", {'page_obj': page_obj})

def car_detail_view(request, car_id):
    car = Car.objects.get(pk=car_id)
    return render(request, "main/detail.html", {'car': car})

def add_car_view(request:HttpRequest):
    if request.method == "POST":
        name = request.POST["name"]
        brand_id = request.POST["brand"]
        brand = Brand.objects.get(id=brand_id)
        colors = request.POST.getlist("colors")
        car = Car.objects.create(name=name, brand=brand, space=request.POST["space"], model_year=request.POST["model_year"])
        car.colors.set(colors)
        car.save()
        messages.success(request, "Car added successfully!")
        return redirect("main:home_view")
    brands = Brand.objects.all()
    colors = Color.objects.all()
    return render(request, "main/create.html", {"brands": brands, "colors": colors})

def update_car_view(request:HttpRequest, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        car.name = request.POST["name"]
        car.space = request.POST["space"]
        car.model_year = request.POST["model_year"]
        car.photo=request.FILES["photo"]
        car.save()
        messages.success(request, "Car updated successfully!")
        return redirect("main:home_view")
    return render(request, "main/update_car.html", {"car": car})



def delete_car_view(request:HttpRequest,car_id):
      
      car = Car.objects.get(pk=car_id)
      car.delete()
      return redirect("main:home_view")