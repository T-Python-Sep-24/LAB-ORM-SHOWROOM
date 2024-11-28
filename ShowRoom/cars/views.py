from django.shortcuts import render, redirect
from django.http import HttpRequest
from brands.models import Brand
from .models import Car, Color, Review
from .forms import CarForm, ColorForm
from django.core.paginator import Paginator
from django.contrib import messages


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

    # Paginate the cars list, show 10 cars per page
    paginator = Paginator(cars, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"cars": page_obj.object_list, "brands": brands, "colors": colors, "page_obj": page_obj}    

    return render(request, "cars/all.html", context)


def details_car_view(request: HttpRequest, car_id: int):
    car = Car.objects.get(pk=car_id)
    context = {"car": car}

    return render(request, "cars/details.html", context)


def new_car_view(request: HttpRequest):
    brands = Brand.objects.all()
    colors = Color.objects.all()
    context = {"brands": brands, "colors": colors}

    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Car created successfully!", "alert-success")
            return redirect("cars:all_cars_view")
        else:
            print("form error: ", car_form.errors)
            messages.error(request, "Error creating car. Please try again later", "alert-warning")

    return render(request, "cars/new.html", context)


def update_car_view(request: HttpRequest, car_id: int):
    brands = Brand.objects.all()
    colors = Color.objects.all()
    car = Car.objects.get(pk=car_id)
    context = {"brands": brands, "colors": colors, "car": car}

    if request.method == "POST":
        # updating an existing object (car) not creating new one
        car_form = CarForm(instance=car, data=request.POST, files=request.FILES)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Car updated successfully!")
            return redirect("cars:all_cars_view")
        else:
            print("form error: ", car_form.errors)
            messages.error(request, "Error updating car. Please try again later")


    return render(request, "cars/update.html", context)


def delete_car_view(request: HttpRequest, car_id: int):
    car = Car.objects.get(pk=car_id)
    car.delete()
    messages.success(request, "Car deleted successfully!", "alert-success")
    
    return redirect("cars:all_cars_view")




def new_color_view(request: HttpRequest):
    if request.method == "POST":
        color_form = ColorForm(request.POST)
        if color_form.is_valid():
            color_form.save()
            return redirect("cars:all_cars_view")
        else:
            print("form error: ", color_form.errors)

    return render(request, "cars/new_color.html")


def update_color_view(request: HttpRequest, color_id: int):
    color = Color.objects.get(pk=color_id)
    context = {"color": color}

    if request.method == "POST":
        color_form = ColorForm(instance=color, data=request.POST)
        if color_form.is_valid():
            color_form.save()
            return redirect("cars:all_cars_view")
        else:
            print("form error: ", color_form.errors)

    return render(request, "cars/update_color.html", context)


def delete_color_view(request: HttpRequest, color_id: int):
    color = Color.objects.get(pk=color_id)
    color.delete()

    return redirect("cars:all_cars_view")


def add_review_view(request:HttpRequest, car_id):
    if not request.user.is_authenticated:
        messages.error(request, "Only registered user can add review","alert-danger")
        return redirect("accounts:sign_in")

    if request.method == "POST":
        car_object = Car.objects.get(pk=car_id)
        new_review = Review(car=car_object,user=request.user,comment=request.POST["comment"],rating=request.POST["rating"])
        new_review.save()

        messages.success(request, "Added Review Successfully", "alert-success")

    return redirect("cars:details_car_view", car_id=car_id)