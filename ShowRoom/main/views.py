from django.shortcuts import render, redirect
from django.http import HttpRequest
from cars.models import Car, Attachment
from brands.models import Brand

# Home page view
def homeView(request: HttpRequest):
    cars = Car.objects.all().order_by('-addedAt')[0:3]
    brands = Brand.objects.all().order_by('founded')[0:3]
    
    response = render(request, 'main/home.html', context={'cars':cars, 'brands': brands})
    return response

#Mode change view
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response

