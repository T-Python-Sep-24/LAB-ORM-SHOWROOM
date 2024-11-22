from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from cars.models import Car, Attachment
from cars.forms import CarForm

def addCarView(request: HttpRequest):

    carData = CarForm()
    response = render(request, 'cars/addCar.html', context={'gearType': Car.Gear.choices, 'fuelType': Car.Fuel.choices, 'bodyType': Car.BodyType.choices})
    
    if request.method == "POST":
        carData = CarForm(request.POST)
        images = request.FILES.getlist('image')
        if carData.is_valid():
            carData.save()
            for img in images:
                Attachment.objects.create(car=carData, image=img)

            messages.success(request, f"'{request.POST['model']}' added successfully.", "alert-success")    
            
        response = redirect('cars:carsDisplayView', 'all')
    
    return response

def displayCarsView(request: HttpRequest, filter: str):

    # if filter == 'all':
    cars = Car.objects.all().order_by('-addedAt')
    response = render(request, 'cars/displayCars.html', context={'cars': cars})
    
    return response
