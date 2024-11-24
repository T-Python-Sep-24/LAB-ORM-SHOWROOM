from django.shortcuts import render, redirect
from django.http import HttpRequest
from brands.models import Brand
from cars.models import Car
# Create your views here.

def home_view(request:HttpRequest):
    brands=Brand.objects.all()
    cars=Car.objects.order_by('-year')[0:2]
    return render(request,'main/home.html',{"brands":brands,"cars":cars})