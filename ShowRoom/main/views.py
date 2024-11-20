from django.shortcuts import render
from django.http import request

# Create your views here.


def home_view(request):
     
     return render(request, 'main/home.html')