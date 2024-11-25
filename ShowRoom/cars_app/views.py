from django.shortcuts import render, redirect, get_object_or_404
from .models import Color, Car  # Import your models
from brands_app.models import Brand 
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse

def all_cars_view(request):
    cars = Car.objects.all()
    return render(request, 'cars_app/all_cars.html', {
        'cars': cars,
    })

def car_detail_view(request, car_id):
    car = Car.objects.get(id=car_id)  # Fetch the specific car based on ID
    return render(request, 'cars_app/car_detail.html', {'car': car})

def new_car_view(request):
    if request.method == 'POST':
        print("POST request received.")
        
        name = request.POST.get('name')
        brand_id = request.POST.get('brand')  # Ensure the name matches the form input
        colors_ids = request.POST.getlist('colors')  # Ensure the name matches the form input
        photo = request.FILES.get('photo')
        specs = request.POST.get('specs')
        model = request.POST.get('model')

        brand = get_object_or_404(Brand, id=brand_id)
        print(brand.id)
        print(colors_ids)


        # Create the new Car instance
        car = Car(
            name=name,  
            brand=brand, 
            photo=photo, 
            specs=specs, 
            model=model
        )

        car.save()

        # Add selected colors to the car
        print(colors_ids)
        for color_id in colors_ids:
            color = Color.objects.get(pk=color_id)
            car.colors.add(color)

        return redirect('cars_app:all_cars_view')  # Redirect to the all cars view

    # Fetch brands and colors for the form if it's a GET request
    brands = Brand.objects.all()
    colors = Color.objects.all()
    
    return render(request, 'cars_app/new_car.html', {
        'brands': brands,
        'colors': colors,
    })


def update_car_view(request):
    return render(request, 'cars_app/update_car.html')

def new_color_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hex_code = request.POST.get('hex_code')
        
        # Create a new Color instance
        Color.objects.create(name=name, hex_code=hex_code)
        
        # Redirect to the all colors view
        return redirect('cars_app:all_colors_view')  # Adjust the URL name as necessary

    return render(request, 'cars_app/new_color.html')

def update_color_view(request):
    return render(request, 'cars_app/update_color.html')

def all_colors_view(request):
    colors = Color.objects.all()  # Complete this function as needed
    return render(request, 'cars_app/all_colors.html', {'colors': colors})






