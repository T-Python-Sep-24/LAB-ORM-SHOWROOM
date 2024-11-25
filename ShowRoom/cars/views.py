from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import CarForm, ColorForm
from brands.models import Brand

from .models import Car, Color, CarReview


# Create your views here.


def all_cars_view(request: HttpRequest):

    cars = Car.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()

    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "GET":
        if 'brand' in request.GET and request.GET['brand'] != 'all':
            brand = Brand.objects.get(pk=request.GET['brand'])
            cars = cars.filter(brand=brand)

        if 'color' in request.GET and request.GET['color'] != 'all':
            color = Color.objects.get(pk=request.GET['color'])
            cars = cars.filter(colors = color)

        if 'keyword' in request.GET:
            keyword = request.GET['keyword']

            cars = Car.objects.filter(
                Q(name__contains=keyword) |
                Q(specs__contains=keyword) |
                Q(model_year__contains=keyword)
            )

    return render(request, 'all_cars.html', context={'cars':cars,'colors':colors,'brands':brands, 'page_obj': page_obj})


def car_details_view(request: HttpRequest, car_id):

    car = Car.objects.get(pk=car_id)
    reviews = CarReview.objects.filter(car=car)


    return render(request, 'car_details.html', context={'car':car, 'reviews':reviews, 'rates':CarReview.Rates.choices})


def add_car_view(request: HttpRequest):
    if not request.user.is_superuser:
        messages.error(request, "Only Admins can add Cars", 'alert-danger')
        return redirect('main:home_view')
    try:
        brands = Brand.objects.all()
        colors = Color.objects.all()
        if request.method == "POST":
            new_car = Car(
                name = request.POST['name'],
                photo = request.FILES['photo'],
                specs = request.POST['specs'],
                model_year = request.POST['model_year'],
                brand = Brand.objects.get(pk=request.POST['brand'])
            )
            new_car.save()
            new_car.colors.set(request.POST.getlist('colors'))
            messages.success(request, "Car was added successfully", "alert-success")
            return redirect("cars:all_cars_view")
    # if request.method == "POST":
    #     car_brand = Brand.objects.filter(name=request.POST['brand'])
    #     car_form = CarForm(request.POST,car_brand, request.FILES)
    #     if car_form.is_valid():
    #         car_form.save()
    #         messages.success(request, "Car was added successfully", "alert-success")
    #         return redirect(request, "cars:all_cars_view")
    #     else:
    #         print("add car form is not valid")
    #         print(request.POST)
    #         print(car_form.errors)
    #         messages.error(request, "Error in adding car", "alert-danger")
        return render(request, 'add_car.html', context={'brands': brands, 'colors': colors})
    except Exception as e:
        print(e)
        messages.error(request, "Error adding this car", "alert-danger")
        return redirect(request, 'cars:all_cars_view')


def update_car_view(request: HttpRequest, car_id):

    if not request.user.is_superuser:
        messages.error(request, "Only Admins can Update Cars", 'alert-danger')
        return redirect('main:home_view')

    brands = Brand.objects.all()

    colors = Color.objects.all()
    car = Car.objects.get(pk=car_id)

    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Car was Updated successfully", "alert-success")
            return redirect("cars:car_details_view", car_id=car_id)
        else:
            print("update Car form is not valid ")
            messages.error(request, "Error in Updating this car", "alert-danger")
    return render(request, 'update_car.html', context={'car':car, 'brands':brands, 'colors': colors})


def delete_car_view(request: HttpRequest, car_id: int):
    if not request.user.is_superuser:
        messages.error(request, "Only Admins can delete Cars", 'alert-danger')
        return redirect('main:home_view')
    try:
        car = Car.objects.get(pk=car_id)
        car.delete()
        messages.success(request,'Car was Deleted successfully', "alert-success")
        return redirect('cars:all_cars_view')
    except Exception as e:
        print(e)
        messages.error(request,'Error in Delete car ', "alert-danger")
        return redirect('cars:all_cars_view')


def new_color_view(request: HttpRequest):

    if not request.user.is_superuser:
        messages.error(request, "Only Admins can add Colors", 'alert-danger')
        return redirect('main:home_view')

    if request.method == "POST":
        color_form = ColorForm(request.POST)
        if color_form.is_valid():
            color_form.save()
            messages.success(request, "Color was added successfully", "alert-success")
        else:
            print("color adding form is not valid")
            messages.error(request,"Error in Adding color", "alert-danger")
        return redirect("main:home_view")
    return render(request, 'new_color.html')

def update_color_view(request: HttpRequest, color_id):

    if not request.user.is_superuser:
        messages.error(request, "Only Admins can update colors", 'alert-danger')
        return redirect('main:home_view')

    color = Color.objects.get(pk=color_id)
    if request.method == "POST":
        color_form = ColorForm(request.POST, instance=color)
        if color_form.is_valid():
            color_form.save()
            messages.success(request, "color updated successfully", "alert-success")
            return redirect("main:home_view")
        else:
            print("Error updating color")
            messages.error(request, "error updating color", "alert-danger")


def delete_color_view(request: HttpRequest, color_id):

    if not request.user.is_superuser:
        messages.error(request, "Only Admins can add Cars", 'alert-danger')
        return redirect('main:home_view')

    try:
        color = Color.objects.get(pk=color_id)
        color.delete()
        messages.success(request, "Color was deleted successfully", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Error deleting this color", "alert-danger")


def add_review_view(request: HttpRequest, car_id):

    try:
        if not request.user.is_authenticated:
            messages.error(request, "Please Login to add reviews", 'alert-danger')
            return redirect('accounts:sign_in')
        if request.method == 'POST':
            new_comment = CarReview(
                car=Car.objects.get(pk=car_id),
                user=request.user,
                comment=request.POST['comment'],
                rating=request.POST['rating'])
            new_comment.save()
            messages.success(request, 'Comment was added successfully', 'alert-success')
        return redirect('cars:car_details_view', car_id = car_id)
    except Exception as e:
        messages.error(request, 'Error in adding your comment', 'alert-danger')
        return render(request,'page_not_found.html')
        print(e)