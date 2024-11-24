from django.shortcuts import render, redirect
from django.http import HttpRequest
from brands.models import Brand
from .models import Car, Color
from .forms import CarForm


# Create your views here.
def all_cars_view(request: HttpRequest):
    brands = Brand.objects.all()
    colors = Color.objects.all()
    cars = Car.objects.all()
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        cars = cars.filter(name__contains=request.GET["search"])
    if "brand" in request.GET and len(request.GET["brand"]) >= 1:
        # ForeignKey: use <fieldname>_id. (field stores the primary key of the related model)
        # Get all cars with brand specific ID 
        cars = cars.filter(brand_id=request.GET["brand"])
    if "color" in request.GET and len(request.GET["color"]) >= 1:
        # ManyToManyField: Django intermediate table to manage the relationship between Car and Color.
        # This checks the car_colors table where color_id =
        cars = cars.filter(colors__id=request.GET["color"])

    context = {"cars": cars, "brands": brands, "colors": colors}    

    return render(request, "cars/all.html", context)


def new_car_view(request: HttpRequest):
    brands = Brand.objects.all()
    colors = Color.objects.all()
    context = {"brands": brands, "colors": colors}

    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect("cars:all_cars_view")
        else:
            print("form error: ", car_form.errors)

    return render(request, "cars/new.html", context)