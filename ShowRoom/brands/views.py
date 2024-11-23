from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def all_brands_view(request: HttpRequest):

    return render(request, "brands/all.html")