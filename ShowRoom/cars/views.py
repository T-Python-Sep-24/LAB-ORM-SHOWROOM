from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .forms import CarForm , ColorForm
from .models import Car , VehiclePhoto , Color
from django.template.loader import get_template


# Create your views here.

def manage_car_view(request, car_id=None):
    car = None
    if car_id:
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            pass

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        
        photo_files = request.FILES.getlist('image')  
        
        if form.is_valid():
            car = form.save()  

            for photo in photo_files:
                VehiclePhoto.objects.create(car=car, image=photo)

            return redirect('/')
    else:
        form = CarForm(instance=car)

    return render(request, 'cars/manage_car.html', {'form': form, 'car': car})


def manage_color_view(request, color_id=None):
    color = None
    if color_id:
        try:
            color = Color.objects.get(pk=color_id)
        except Color.DoesNotExist:
            pass

    if request.method == "POST":
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            color = form.save()
            return redirect('/')
    else:
        form = ColorForm(instance=color)

    try:
        get_template('cars/colors/manage_color.html')
    except Exception as e:
        print(f"Error loading template: {e}")

    return render(request, 'cars/colors/manage_color.html', {'form': form, 'color': color})

