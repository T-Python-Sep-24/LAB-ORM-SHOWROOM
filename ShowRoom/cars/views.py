from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse

from django.contrib import messages
from . models import Car , Color
from brands .models import Brand

# Create your views here.



def all_cars_view(request:HttpRequest):
    cars = Car.objects.all()
    return render(request, 'cars/all_cars.html', {'cars': cars})


def new_car_view(request:HttpRequest):
    pass 



















def new_color_view(request: HttpRequest):
    if request.method == "POST":
        new_color = Color(
            name=request.POST["name"],
            hex_value=request.POST["hex_value"]
        )
        new_color.save()
        return redirect('cars:new_color')  

    return render(request, 'cars/new_color.html')


def update_color_view(request: HttpRequest, color_id):
    
    color = Color.objects.get(pk=color_id)

    if request.method == "POST":
        color.name = request.POST["name"]
        color.hex_value = request.POST["hex_value"]
        color.save()
        return redirect('cars:update_color', color_id=color.id)  

    return render(request, 'cars/update_color.html', {'color': color})