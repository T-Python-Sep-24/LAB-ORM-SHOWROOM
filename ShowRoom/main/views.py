from django.shortcuts import render
from django.http import HttpRequest
from cars.models import Car

# Create your views here.
def home_view(request: HttpRequest):
    cars = Car.objects.all().order_by("-id")[0:4]
    context = {"cars": cars}

    return render(request, "main/index.html", context)