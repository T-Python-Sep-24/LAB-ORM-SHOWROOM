from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html') 

def all_cars(request):
    return render(request, 'main/all_cars.html') 


