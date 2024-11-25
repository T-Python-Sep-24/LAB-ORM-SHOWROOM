from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from datetime import datetime, date

from .models import Contact
from .forms import ContactForm

from cars.models import Car
from brands.models import Brand

from django.core.mail import EmailMessage


def home_view(request:HttpRequest):
    cars = Car.objects.filter(year__gt=datetime(2024, 12, 1))
    brands = Brand.objects.filter(founded_at__gt=datetime(1930, 1, 1))

    return render(request, 'main/home.html', {'cars': cars, 'brands': brands})

def contact_view(request:HttpRequest):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            
            
            
            return redirect('main:home_view')
        else:
            return render(request, "main/contact.html")

    return render(request, 'main/contact.html' )