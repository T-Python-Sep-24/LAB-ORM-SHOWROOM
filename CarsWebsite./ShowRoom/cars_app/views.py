from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Car, Color
from brands_app.models import Brand
from django.contrib import messages

def all_cars_view(request: HttpRequest):
    # Logic to retrieve all cars with pagination
    cars = Car.objects.all()
    return render(request, 'cars_app/all_cars.html', {'cars': cars})

def car_detail_view(request: HttpRequest, car_id):
    # Logic to retrieve a car by ID
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars_app/car_detail.html', {'car': car})

def new_car_view(request: HttpRequest):
    # Logic for creating a new car
    if request.method == 'POST':
        name = request.POST.get('name')
        brand_id = request.POST.get('brand')
        color_ids = request.POST.getlist('colors')
        photo = request.FILES.get('photo')
        specs = request.POST.get('specs')
        model = request.POST.get('model')

        brand = get_object_or_404(Brand, id=brand_id)
        car = Car.objects.create(name=name, brand=brand, photo=photo, specs=specs, model=model)
        car.colors.set(color_ids)  # Set the many-to-many relationship

        messages.success(request, "Car added successfully!")
        return redirect('all_cars')

    brands = Brand.objects.all()
    colors = Color.objects.all()
    return render(request, 'cars_app/add_new_car.html', {'brands': brands, 'colors': colors})

def update_car_view(request: HttpRequest, car_id):
    # Logic for updating a car
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        car.name = request.POST.get('name')
        car.brand = get_object_or_404(Brand, id=request.POST.get('brand'))
        car.specs = request.POST.get('specs')
        car.model = request.POST.get('model')

        if 'photo' in request.FILES:
            car.photo = request.FILES['photo']
        
        car.colors.set(request.POST.getlist('colors'))  # Update the many-to-many relationship
        car.save()

        messages.success(request, "Car updated successfully!")
        return redirect('car_detail', car_id=car.id)

    brands = Brand.objects.all()
    colors = Color.objects.all()
    return render(request, 'cars_app/update_car.html', {'car': car, 'brands': brands, 'colors': colors})