from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse
from cars.models  import Car
from brands.models import Brand

def home_view(request:HttpRequest):
    if request.user.is_authenticated:
        print(request.user.first_name)
    else:
        print("...........!")
    brands =Brand.objects.all()[:3]  
    cars = Car.objects.all()[:3]  

    return render(request, 'main/home.html', {'brands': brands,'cars': cars,})  