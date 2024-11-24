from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
 
def home(request: HttpRequest):
    return render(request, "main/base.html")
