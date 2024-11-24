from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from cars.models import Car
from brands.models import Brand

# Create your views here.
def home_view(request:HttpRequest):
 
    car = Car.objects.all()[:3] 
    return render(request, 'main/index.html', {'car': car})