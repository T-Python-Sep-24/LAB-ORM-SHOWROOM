from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from cars.models import Car, Attachment, Color
from cars.forms import CarForm, ColorForm
from brands.models import Brand


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
    colors = Color.objects.all()
    brands = Brand.objects.all()
    response = render(request, 'cars/addCar.html', context={'brands': brands, 'colors': colors, 'gearTypes': Car.Gear.choices, 'fuelTypes': Car.Fuel.choices, 'bodyTypes': Car.BodyType.choices})
    
    if request.method == "POST":
        carData = CarForm(request.POST)
        images = request.FILES.getlist('images')
        if carData.is_valid():
            car:Car = carData.save(commit=False)
            car.save()
            car.colors.set(request.POST.getlist("colors"))
            for img in images:
                Attachment.objects.create(car=car, image=img)
            messages.success(request, f"'{request.POST['model']}' was added successfully.", "alert-success")
        else:
            messages.error(request, f"'{request.POST['model']}' wasn't added.", "alert-danger")
            
        #response = redirect('cars:carsDisplayView', 'all')
        response = redirect('main:homeView')
    
    return response

# Update car view
def updateCarView(request: HttpRequest, carid:int):

    try:
        car = Car.objects.get(pk=carid)
    except Exception:
        response = render(request, '404.html')
    else:
        colors = Color.objects.all()
        brands = Brand.objects.all()
        carImages = Attachment.objects.filter(car=car)
        response = render(request, 'cars/updateCar.html', context={'car': car, 'carImgs': carImages, 'brands': brands, 'colors': colors, 'gearTypes': Car.Gear.choices, 'fuelTypes': Car.Fuel.choices, 'bodyTypes': Car.BodyType.choices})
        
        if request.method == "POST":
            carData = CarForm(request.POST, instance=car)
            images = request.FILES.getlist('images')
            if carData.is_valid():
                car:Car = carData.save(commit=False)
                car.save()
                car.colors.set(request.POST.getlist("colors"))
                if images:
                    Attachment.objects.filter(car=car).delete()
                    for img in images:
                        Attachment.objects.create(car=car, image=img)
                
                messages.success(request, f"'{request.POST['model']}' was updated successfully.", "alert-success")
            else:
                messages.error(request, f"'{request.POST['model']}' wasn't updated.", "alert-danger")
                
            #response = redirect('cars:carsDisplayView', 'all')
            response = redirect('main:homeView')

    return response

def displayCarsView(request: HttpRequest, filter: str):

    bodyTypes = Car.BodyType.choices
    carImages = Attachment.objects.all()

    if filter == 'all':
        cars = Car.objects.all().order_by('-addedAt')
    else:
        cars = Car.objects.filter(bodyType=filter).order_by('-addedAt')

    response = render(request, 'cars/displayCars.html', context={'cars': cars, 'selected': filter, 'bodyTypes': bodyTypes, 'carImages': carImages})
    
    return response
