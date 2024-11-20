from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse


# Create your views here.

def all_cars_view(request:HttpRequest):

    return render(request, 'cars/all_cars.html')
