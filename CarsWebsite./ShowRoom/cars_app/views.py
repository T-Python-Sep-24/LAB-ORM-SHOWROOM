from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
# Create your views here.

def all_cars_view(request:HttpRequest):
    # Logic to retrieve all cars
    return render(request, 'cars_app/all_cars.html')

def car_detail_view(request:HttpRequest, car_id):
    # Logic to retrieve a car by ID
    return render(request, 'cars_app/car_detail.html')

def new_car_view(request:HttpRequest):
    # Logic for creating a new car
    return render(request, 'cars_app/add_new_car.html')

def update_car_view(request:HttpRequest, car_id):
    # Logic for updating a car
    return render(request, 'cars_app/update_car.html')