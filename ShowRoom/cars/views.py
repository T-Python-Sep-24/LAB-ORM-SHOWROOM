from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import CarForm, ColorForm
from .models import Car, Color

# Create your views here.
def all_cars_view(request: HttpRequest):
    cars = Car.objects.all()
    return render(request, 'all_cars.html', context={'cars':cars})

def car_details_view(request: HttpRequest, car_id):

    car = Car.objects.get(pk=car_id)

    return render(request, 'car_details.html', context={'car':car})

def update_car_view(request: HttpRequest, car_id):

    car = Car.objects.get(pk=car_id)
    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Car was added successfully", "alert-success")
            return redirect("cars:car_details_view", car_id=car_id)
        else:
            print("add Car form is not valid ")
            messages.error(request, "Error in Adding this car", "alert-danger")

def delete_car_view(request: HttpRequest, car_id: int):

    try:
        car = Car.objects.get(pk=car_id)
        car.delete()
        return redirect(request, 'all_cars_view')
    except Exception as e:
        print(e)


def new_color_view(request: HttpRequest):

    if request.method == "POST":
        color_form = ColorForm(request.POST)
        if color_form.is_valid():
            color_form.save()
            messages.success(request, "Color was added successfully", "alert-success")
        else:
            print("color adding form is not valid")
            messages.error(request,"Error in Adding color", "alert-danger")
        return redirect(request, "main:home_view")


def update_color_view(request: HttpRequest, color_id):

    color = Color.objects.get(pk=color_id)
    if request.method == "POST":
        color_form = ColorForm(request.POST, instance=color)
        if color_form.is_valid():
            color_form.save()
            messages.success(request, "color updated successfully", "alert-success")
            return redirect(request, "main:home_view")
        else:
            print("Error updating color")
            messages.error(request, "error updating color", "alert-danger")