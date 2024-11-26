from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Car, Color,Review
from brands.models import Brand
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib import messages

def all_cars_view(request:HttpRequest):
    cars = Car.objects.all()
    paginator = Paginator(cars, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "main/all_cars.html", {'page_obj': page_obj})

def car_detail_view(request, car_id):
    car = Car.objects.get(pk=car_id)
    reviews = Review.objects.filter(car=car)
    return render(request, "main/detail.html", {'car': car,"reviews":reviews})

def add_car_view(request:HttpRequest):
    if not request.user.is_staff:
        messages.success(request,"only staff can add","alert-warning")
        return redirect("main:home_view")
    if request.method == "POST":
        photo = request.FILES["photo"]
        name = request.POST["name"]
        brand_id = request.POST["brand"]
        brand = Brand.objects.get(id=brand_id)
       
    
        car = Car.objects.create(name=name, brand=brand, space=request.POST["space"], model_year=request.POST["model_year"],photo=photo)
        
        car.save()
        messages.success(request, "Car added successfully!")
        return redirect("main:home_view")
    brands = Brand.objects.all()
    
    return render(request, "main/create.html", {"brands": brands})

def update_car_view(request:HttpRequest, car_id):
    if not request.user.is_staff:
       messages.error(request,"only registerd user can review","alert-Warning")
       return redirect("main:home_view")
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        car.name = request.POST["name"]
        car.space = request.POST["space"]
        car.model_year = request.POST["model_year"]
        car.photo=request.FILES["photo"]
        car.save()
        messages.success(request, "Car updated successfully!","alert-success")
        return redirect("main:home_view")
    return render(request, "main/update_car.html", {"car": car})



def delete_car_view(request:HttpRequest,car_id):
    if not request.user.is_staff:
       messages.error(request,"only registerd user can review","alert-Warning")
       return redirect("main:home_view")     
    car = Car.objects.get(pk=car_id)
    car.delete()
    return redirect("main:home_view")




def add_review(request:HttpRequest,car_id):
   if not request.user.is_authenticated:
       messages.error(request,"only registerd user can review","alert-Warning")
       return redirect("account:sign_up")
   if request.method == "POST":
    car_object=Car.objects.get(pk=car_id)
    new_review=Review(car=car_object,user=request.user,coment=request.POST["coment"])
    new_review.save()
    messages.success(request,"review added successfuly","alert-success")
   return redirect("cars:car_detail_view",car_id=car_id)



