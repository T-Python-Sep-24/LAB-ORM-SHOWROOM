from django.shortcuts import render, redirect
from .models import Brand, Color, Car  # Import your models
#from django.db import IntegrityError
from .forms import CarForm  # Import the CarForm
from django.contrib import messages
from django.http import HttpRequest

def all_cars_view(request):
    cars = Car.objects.all()
    return render(request, 'cars_app/all_cars.html', {
        'cars': cars,
    })

def car_detail_view(request, car_id):
    car = Car.objects.get(id=car_id)  # Fetch the specific car based on ID
    return render(request, 'cars_app/car_detail.html', {'car': car})

def new_car_view(request: HttpRequest):
    # Fetch all brands and colors to display in the form
    brands = Brand.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect('cars_app:all_cars_view')
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = CarForm()  # Create a new instance of the form for GET requests

    return render(request, 'cars_app/new_car.html', {
        'form': form,
        'brands': brands,  # Pass brands to the template
        'colors': colors,  # Pass colors to the template
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






