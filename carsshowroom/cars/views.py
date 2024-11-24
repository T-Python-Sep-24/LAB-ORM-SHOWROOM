from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Car,Color,Review
from brands.models import Brand

from .forms import CarForm,ColorForm

# Create your views here.


def all_cars_view(request:HttpRequest):
    cars=Car.objects.all()
    brands=Brand.objects.all()
    colors=Color.objects.all()
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        cars = Car.objects.filter(name__contains=request.GET["search"])
        
    if "brand" in request.GET and request.GET["brand"]:
        cars = cars.filter(brand__id=request.GET["brand"])

    if "color" in request.GET and request.GET["color"]:
        cars = cars.filter(colors__id=request.GET["color"])
    
    page_number = request.GET.get("page", 1)
    paginator = Paginator(cars, 10)
    car_page = paginator.get_page(page_number)
    return render(request,"cars/all_cars.html",context={"cars":car_page,"colors":colors,"brands":brands})

def new_car_view(request:HttpRequest):
    if request.user.is_superuser:
        car_form=CarForm()

        colors=Color.objects.all()
        brands=Brand.objects.all()
        if request.method =='POST':
            car_form=CarForm(request.POST,request.FILES)
            if car_form.is_valid():
                car_form.save()
                messages.success(request,"Car has been added successfully ","alert-success")
                return redirect("cars:all_cars_view")
            else:
                messages.error(request,car_form.errors,"alert-danger")
        return render(request,"cars/new_car.html",context={'car_form':car_form, 'colors':colors,'brands':brands})
    else:
        messages.error(request,"access denid you should be the manager to access this page!!","alert-danger")
        return redirect('main:home_view')

def car_detail_view(request:HttpRequest,car_id:int):
    car=Car.objects.get(pk=car_id)
    
    reviews = Review.objects.filter(car=car)
    return render(request,"cars/car_detail.html",{"car":car,"reviews":reviews})

def car_update_view(request:HttpRequest,car_id:int):
    if request.user.is_superuser:
        car=Car.objects.get(pk=car_id)
        colors=Color.objects.all()
        brands=Brand.objects.all()
        if request.method =='POST':
            car_form=CarForm(instance=car,data=request.POST,files=request.FILES)
            if car_form.is_valid():
                car_form.save()
                messages.success(request,"Car has been updated successfully ","alert-success")
                return redirect("cars:car_detail_view", car_id=car.id)
            else:
                messages.error(request,car_form.errors,"alert-danger")
        return render(request,"cars/update_car.html",context={'car':car, 'colors':colors,'brands':brands})
    else:
        messages.error(request,"access denid you should be the manager to access this page!!","alert-danger")
        return redirect('main:home_view')


def delete_car_view(request:HttpRequest,car_id:int):
    if request.user.is_superuser:
        try:
            car=Car.objects.get(pk=car_id)
            car.delete()
            messages.success(request, f"Deleted {car.name} successfully", "alert-success")
        except Exception as e:
            print(e)
            messages.error(request, f"Couldn't Delete {car.name} ", "alert-danger")
        return redirect ("cars:all_cars_view")
    else:
        messages.error(request,"access denid you should be the manager to access this page!!","alert-danger")
        return redirect('main:home_view')

def all_colors_view(request:HttpRequest):
    colors=Color.objects.all()
    return render(request,"colors/all_colors.html",context={'colors':colors})

def new_color_view(request:HttpRequest):
    if request.user.is_superuser:
        color_form=ColorForm()
        if request.method =='POST':
            color_form=ColorForm(request.POST)
            if color_form.is_valid():
                color_form.save()
                messages.success(request,"Color has been added successfully ","alert-success")
                return redirect("cars:all_colors_view")
            else:
                messages.error(request,color_form.errors,"alert-danger")
        return render(request,"colors/new_color.html",context={'color_form':color_form})
    else:
        messages.error(request,"access denid you should be the manager to access this page!!","alert-danger")
        return redirect('main:home_view')


def color_update_view(request:HttpRequest,color_id:int):
    if request.user.is_superuser:
        color=Color.objects.get(pk=color_id)
        if request.method =='POST':
            color_form=ColorForm(request.POST)
            if color_form.is_valid():
                color_form.save()
                messages.success(request,"Color has been added successfully ","alert-success")
                return redirect("cars:all_colors_view")
            else:
                messages.error(request,color_form.errors,"alert-danger")
        return render(request,"colors/update_color.html",context={'color':color})
    else:
        messages.error(request,"access denid you should be the manager to access this page!!","alert-danger")
        return redirect('main:home_view')


def delete_color_view(request:HttpRequest,color_id:int):
    if request.user.is_superuser:
        try:
            color=Color.objects.get(pk=color_id)
            color.delete()
            messages.success(request, f"Deleted {color.name} successfully", "alert-success")
        except Exception as e:
            print(e)
            messages.error(request, f"Couldn't Delete {color.name} ", "alert-danger")
        return redirect ("cars:all_colors_view")
    else:
        messages.error(request,"access denid you should be the manager to access this page!!","alert-danger")
        return redirect('main:home_view')



def add_review_view(request:HttpRequest,car_id:int):
    car_obj=Car.objects.get(pk=car_id)
    
    if request.method =='POST' and request.user.is_authenticated:
        new_review=Review(car=car_obj,name=request.user.username,comment=request.POST['comment'])
        new_review.save()
        messages.success(request,f"review hsa been added to {car_obj.name}","alert-success")
        return redirect("cars:car_detail_view", car_id=car_obj.id)
    else:
        messages.error(request,"Sign in or Sign up first to add a comment","alert-warning")
        return redirect('main:home_view')
    
    



