from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Car, Color
from brands_app.models import Brand
from django.contrib import messages
from .form import CarForm  


def all_cars_view(request: HttpRequest):
   
    cars = Car.objects.all()
    return render(request, 'cars_app/all_cars.html', {'cars': cars})

def car_detail_view(request: HttpRequest, car_id: int):
   
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars_app/car_detail.html', {'car': car})



def new_car_view(request: HttpRequest):
    
    form = CarForm() 
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            messages.success(request, "Car added successfully!")
            return redirect('cars_app:all_cars_view')  # Redirect to all cars view

    return render(request, 'cars_app/add_new_car.html', {'form': form})  # Ensure form is always defined

def update_car_view(request: HttpRequest, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()  
            messages.success(request, "Car updated successfully!")
            return redirect('cars_app:car_detail_view', car_id=car.id)  
    else:
        form = CarForm(instance=car)
    
    return render(request, 'cars_app/update_car.html', {'form': form, 'car': car})

def delete_car_view(request: HttpRequest, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        car.delete()  
        messages.success(request, "Car deleted successfully!")
        return redirect('cars_app:all_cars_view')  

        return render(request, 'cars_app/delete_car.html', {'car': car})