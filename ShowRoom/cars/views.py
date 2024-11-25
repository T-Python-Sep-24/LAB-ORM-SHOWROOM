from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Car, Color, Review
from .forms import CarForm, ColorForm

from brands.models import Brand

from django.core.paginator import Paginator

from django.contrib import messages

from django.contrib.auth.decorators import login_required


def all_cars_view(request:HttpRequest, filter):
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    if filter == 'all':
        cars = Car.objects.all()
    else:
        cars = Car.objects.filter(colors__name__in=[filter])
        
    page_number = request.GET.get("page", 1)
    paginator = Paginator(cars, 4)
    cars_page = paginator.get_page(page_number)
    
    return render(request, "cars/all_cars.html", {'cars': cars_page,
                                                  'filter': filter,
                                                  'brands': brands,
                                                  'colors': colors,})

def car_detail_view(request:HttpRequest, car_id:int):
    car = Car.objects.get(pk=car_id)
    
    return render(request, "cars/car_detail.html", {'car': car, 'rating': Review.RatingChoices.choices})

def new_car_view(request:HttpRequest):
    car_form = CarForm()
    
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Added Car Successfuly!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", car_form.errors)
            messages.error(request, "Couldn't Add Car!", "alert-danger")
            
    return render(request, "cars/car_add.html", 
                           {
                            'categories': Car.Category.choices, 
                            'doors': Car.DoorChoices.choices, 
                            'colors': colors, 
                            'brands': brands
                            })

def car_update_view(request:HttpRequest, car_id:int):
    car = Car.objects.get(pk=car_id)
    
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    if request.method == "POST":
        car_form = CarForm(instance=car, data=request.POST, files=request.FILES)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, "Updated Color Successfuly!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", car_form.errors)
            messages.error(request, "Couldn't Update Car!", "alert-danger")
            
        return redirect("cars:car_detail_view", car_id=car_id)
    
    return render(request, "cars/car_update.html", {
                            'car': car,
                            'categories': Car.Category.choices, 
                            'doors': Car.DoorChoices.choices, 
                            'colors': colors, 
                            'brands': brands
                            })

def car_delete_view(request:HttpRequest,  car_id:int):
    try:
        car = Car.objects.get(pk=car_id)
        car.delete()
        messages.success(request, "Deleted Car Successfuly!", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Couldn't Delete Car!", "alert-danger")
    
    return redirect("main:home_view")

# @login_required
def add_review_view(request:HttpRequest, car_id):
    if not request.user.is_authenticated:
        messages.error(request, "Only registered user can add review","alert-danger")
        return redirect("accounts:sign_in")
 
    if request.method == "POST":
        car = Car.objects.get(pk=car_id)
        review = Review(car=car,user=request.user,comment=request.POST["comment"],rating=request.POST["rating"])
        review.save()

        messages.success(request, "Added Review Successfully", "alert-success")

    return redirect("cars:car_detail_view", car_id=car_id)


def new_color_view(request:HttpRequest):
    color_form = ColorForm()
    
    if request.method == "POST":
        color_form = ColorForm(request.POST)
        if color_form.is_valid():
            color_form.save()
            messages.success(request, "Added Color Successfuly!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", color_form.errors)
            messages.error(request, "Couldn't Add Color!", "alert-danger")
            
    return render(request, "cars/color_add.html")


def search_cars_view(request:HttpRequest):
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        cars = Car.objects.filter(name__contains=request.GET["search"])
        filter_by = request.GET["search"]
        
        
        if "order_by" in request.GET and request.GET["order_by"] == "year":
            cars = cars.order_by("-year")
            filter_by = 'order by year'
        if "filter_brand" in request.GET and request.GET["filter_brand"] != '':
            cars = cars.filter(brand__id=request.GET['filter_brand'])
            filter_by = Brand.objects.get(pk=int(request.GET['filter_brand'])).name
        if "filter_color" in request.GET and request.GET["filter_color"] != '':
            cars = cars.filter(colors__id__in=[request.GET['filter_color']])
            filter_by = Color.objects.get(pk=int(request.GET['filter_color'])).name
            
    elif "order_by" in request.GET and request.GET["order_by"] == "year":
        cars = Car.objects.all().order_by("-year")
        filter_by = 'order by year'
        
        if "filter_brand" in request.GET and request.GET["filter_brand"] != '':
            cars = cars.filter(brand__id=request.GET['filter_brand'])
            filter_by = Brand.objects.get(pk=int(request.GET['filter_brand'])).name
        if "filter_color" in request.GET and request.GET["filter_color"] != '':
            cars = cars.filter(colors__id__in=[request.GET['filter_color']])
            filter_by = Color.objects.get(pk=int(request.GET['filter_color'])).name
            
    elif "filter_brand" in request.GET and request.GET["filter_brand"] != '':
        cars = Car.objects.filter(brand__id=request.GET['filter_brand'])
        filter_by = Brand.objects.get(pk=int(request.GET['filter_brand'])).name
        
        if "filter_color" in request.GET and request.GET["filter_color"] != '':
            cars = cars.filter(colors__id__in=[request.GET['filter_color']])
            filter_by = f'{Color.objects.get(pk=int(request.GET['filter_color'])).name} - {filter_by}'
        if "order_by" in request.GET and request.GET["order_by"] == "year":
            cars = cars.order_by("-year")
            filter_by = 'order by year'
        
    elif "filter_color" in request.GET and request.GET["filter_color"] != '':
        cars = Car.objects.filter(colors__id__in=[int(request.GET['filter_color'])])
        filter_by = Color.objects.get(pk=int(request.GET['filter_color'])).name
        
        if "filter_brand" in request.GET and request.GET["filter_brand"] != '':
            cars = cars.filter(brand__id=request.GET['filter_brand'])
            filter_by = f'{Brand.objects.get(pk=int(request.GET['filter_brand'])).name} - {filter_by}' 
            
        if "order_by" in request.GET and request.GET["order_by"] == "year":
            cars = cars.order_by("-year")
            filter_by = 'order by year'
            
        
    else:
        cars = []
    
    return render(request, "cars/car_search.html", {'cars': cars,
                                                    'brands': brands,
                                                    'colors': colors,
                                                    'filter_by': filter_by})

    
    
    