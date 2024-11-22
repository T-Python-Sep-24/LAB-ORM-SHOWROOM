from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from cars.models import Car, Attachment, Color
from cars.forms import CarForm, ColorForm


# Add color view
def addColorView(request:HttpRequest):
    colorData = ColorForm()
    response = render(request, 'colors/addColor.html')
    if request.method == "POST":
        colorData = ColorForm(request.POST, request.FILES)
        if colorData.is_valid():
            colorData.save()
            messages.success(request, f"Color '{request.POST['name']}' was added successfully.", "alert-success")
        else:
            messages.error(request, f"Color '{request.POST['name']}' wasn't added. {colorData.errors}", "alert-danger")
            
        response = redirect('main:homeView')

    return response

# Update color view
def updateColorView(request:HttpRequest, clrId:int):

    try:
        color = Color.objects.get(pk=clrId)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'colors/updateColor.html', context={'color': color})
        if request.method == "POST":
            colorData = ColorForm(request.POST, request.FILES, instance=color)
            if colorData.is_valid():
                colorData.save()
                messages.success(request, f"Color '{request.POST['name']}' was updated successfully.", "alert-success")
            else:
                messages.error(request, f"Color '{request.POST['name']}' wasn't updated. {colorData.errors}", "alert-danger")
                
            response = redirect('main:homeView')

    return response

# Add car view
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

            messages.success(request, f"'{request.POST['model']}' was added successfully.", "alert-success")    
            
        #response = redirect('cars:carsDisplayView', 'all')
        response = redirect('main:homeView')
    
    return response

def displayCarsView(request: HttpRequest, filter: str):

    # if filter == 'all':
    cars = Car.objects.all().order_by('-addedAt')
    response = render(request, 'cars/displayCars.html', context={'cars': cars})
    
    return response
