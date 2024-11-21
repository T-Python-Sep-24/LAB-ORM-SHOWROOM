from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def home_view(request:HttpRequest):

    return render(request, 'main/home.html')

def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html' )