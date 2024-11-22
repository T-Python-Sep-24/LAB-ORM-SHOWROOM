from django.shortcuts import render, redirect
from django.http import HttpRequest
from cars.models import Car

# Home page view
def homeView(request: HttpRequest):
    cars = Car.objects.all().order_by('addedAt')[0:3]
    response = render(request, 'main/home.html', context={'cars':cars})
    return response

#Contact us view


#Mode change view
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response

