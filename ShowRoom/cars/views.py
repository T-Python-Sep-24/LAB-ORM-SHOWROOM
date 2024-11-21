from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        car = None

    if car is None:
        return render(request, 'cars/car_not_found.html', status=404)
    
    return render(request, 'cars/car_detail.html', {'car': car})
