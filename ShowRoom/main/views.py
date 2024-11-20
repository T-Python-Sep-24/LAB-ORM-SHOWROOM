from django.shortcuts import render
from django.http import HttpRequest

# Home page
def homeView(request: HttpRequest):
    response = render(request, 'main/home.html')
    return response
