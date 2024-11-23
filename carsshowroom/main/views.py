from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from django.core.paginator import Paginator
from cars.models import Car

# Create your views here.

def home_view(request:HttpRequest):
    cars=Car.objects.filter().order_by('-id')[:4]
    return render(request,'main/index.html',context={'cars':cars})