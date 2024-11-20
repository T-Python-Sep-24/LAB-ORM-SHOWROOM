from django.shortcuts import render, redirect
from django.http import HttpRequest

# Home page view
def homeView(request: HttpRequest):
    response = render(request, 'main/home.html')
    return response

#Mode change view
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response

#Contact us view
