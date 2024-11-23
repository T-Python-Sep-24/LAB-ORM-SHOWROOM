from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def all_cars_view(request: HttpRequest):

    return render(request, "cars/all.html")