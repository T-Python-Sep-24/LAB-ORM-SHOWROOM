from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Car, Color
from .forms import CarForm, ColorForm

def all_cars(request: HttpRequest):
    cars = Car.objects.all()
    return render(request, "cars/all_cars.html", {"cars": cars})

def car_detail(request: HttpRequest, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponse("Car not found", status=404)
    return render(request, "cars/car_detail.html", {"car": car})

def new_car(request: HttpRequest):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect("cars:all_cars")
    else:
        form = CarForm()
    return render(request, "cars/new_car.html", {"form": form})

def update_car(request: HttpRequest, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponse("Car not found", status=404)
    
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect("cars:all_cars")
    else:
        form = CarForm(instance=car)
    return render(request, "cars/update_car.html", {"form": form, "car": car})

def delete_car(request: HttpRequest, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
        messages.success(request, "Car deleted successfully!")
    except Car.DoesNotExist:
        messages.error(request, "Car not found.")
    return redirect("cars:all_cars")


def all_colors(request):
    colors = Color.objects.all()
    return render(request, 'cars/all_colors.html', {'colors': colors})

def new_color(request: HttpRequest):
    if request.method == "POST":
        form = ColorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Color added successfully!")
            return redirect("cars:all_colors")
    else:
        form = ColorForm()
    return render(request, "cars/new_color.html", {"form": form})

def update_color(request: HttpRequest, color_id):
    try:
        color = Color.objects.get(id=color_id)
    except Color.DoesNotExist:
        return HttpResponse("Color not found", status=404)
    
    if request.method == "POST":
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, "Color updated successfully!")
            return redirect("cars:all_cars")
    else:
        form = ColorForm(instance=color)
    return render(request, "cars/update_color.html", {"form": form, "color": color})

def delete_color(request: HttpRequest, color_id):
    try:
        color = Color.objects.get(id=color_id)
        color.delete()
        messages.success(request, "Color deleted successfully!")
    except Color.DoesNotExist:
        messages.error(request, "Color not found.")
    return redirect("cars:all_cars")


