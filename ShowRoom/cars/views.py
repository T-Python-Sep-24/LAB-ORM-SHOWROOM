from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Car,Color,Photo
from .forms import ColorForm,CarForm,PhotoForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def all_cars_view(request:HttpRequest):
    return render(request,'cars/all_cars.html')


def detail_car_view(request:HttpRequest,car_id):
    return render(request,'cars/detail_car.html')


def new_car_view(request:HttpRequest):
    return render(request,'cars/new_car.html')


def update_car_view(request:HttpRequest,car_id):
    return render(request,'cars/update_car.html')


def new_color_view(request:HttpRequest):
    if request.method=="POST":
        color_form=ColorForm(request.POST,request.FILES)
        if color_form.is_valid():
              color_form.save()
              messages.success(request, 'The color has been added successfully!','alert-success')
              return redirect("cars:new_color_view")
        else:
            print("form is not valid")
            print(color_form.errors)
    return render(request,'cars/new_color.html')


def update_color_view(request:HttpRequest,color_id):
    try:
        color=Color.objects.get(pk=color_id)
        if request.method=="POST":
            color_form=ColorForm(request.POST,request.FILES,instance=color)
            if color_form.is_valid():
                color_form.save()
                messages.success(request, 'The color has been updated successfully!','alert-success')
                return redirect('cars:update_color_view',color_id=color.id)
            else:
                print("form is not valid")
                print(color_form.errors)
                return redirect('main:home_view') 
        else:   
            color_form = ColorForm(instance=color)
        return render(request,'cars/update_color.html',{"color":color})                

    except Color.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')
    