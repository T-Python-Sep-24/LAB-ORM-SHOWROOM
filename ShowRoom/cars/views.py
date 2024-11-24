from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Car,Color,Photo
from brands.models import Brand
from .forms import ColorForm,CarForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def all_cars_view(request:HttpRequest):
    cars=Car.objects.all()
    brands=Brand.objects.all()
    colors=Color.objects.all()
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        cars = cars.filter(name__icontains=request.GET["search"])

    if "filter_by_brand" in request.GET and request.GET["filter_by_brand"]:
        cars = cars.filter(brand__id=request.GET["filter_by_brand"])

    if "filter_by_color" in request.GET and request.GET["filter_by_color"]:
        cars = cars.filter(colors__id=request.GET["filter_by_color"]) 
    
    p=Paginator(cars,4)
    page=request.GET.get('page',1)
    cars_list=p.get_page(page)
    return render(request,'cars/all_cars.html',{"cars":cars_list,"colors":colors,"brands":brands})


def detail_car_view(request:HttpRequest,car_id):
    try:    
        car =Car.objects.get(pk=car_id)
        car_colors=car.colors.all()
        car_photos=car.photos.all()[1:]     
        return render(request,'cars/detail_car.html',{"car":car,"car_colors":car_colors,"car_photos":car_photos})
    except Car.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')


def new_car_view(request:HttpRequest):
    brands=Brand.objects.all()
    colors=Color.objects.all()
    if request.method=="POST":
        car_form=CarForm(request.POST,request.FILES)
        if car_form.is_valid():
              car=car_form.save()
              if request.FILES.getlist('photos'):
                    photos = request.FILES.getlist('photos')
                    for photo in photos:
                        Photo.objects.create(car=car, image=photo) 
              messages.success(request, 'The car has been added successfully!','alert-success')
              return redirect("cars:new_car_view")
        else:
            print("form is not valid")
            print(car_form.errors)
    return render(request,'cars/new_car.html',{"brands":brands,"colors":colors,"FuelChoices":Car.FuelChoices.choices})

def update_car_view(request:HttpRequest,car_id):
    try:    
        car =Car.objects.get(pk=car_id)
        brands=Brand.objects.all()
        colors=Color.objects.all()
        car_colors=car.colors.all()
        car_photos=car.photos.all()
        if request.method=="POST":
            print(request.POST.getlist('colors')) 
            car_form=CarForm(request.POST,request.FILES,instance=car)
            if request.POST.getlist('colors'):
                car.colors.set(request.POST.getlist('colors'))
            if car_form.is_valid():
                car=car_form.save()
                
                if request.FILES.getlist('photos'):
                    car.photos.all().delete()#clear previose images
                    photos = request.FILES.getlist('photos')
                    for photo in photos:
                        Photo.objects.create(car=car, image=photo)  
                car.save()         
                messages.success(request, 'The car has been updated successfully!','alert-success')
                return redirect("cars:update_car_view",car_id=car.id)
            else:
                print("form is not valid")
                print(car_form.errors)
        else:   
            car_form = CarForm(instance=car)        
        return render(request,'cars/update_car.html',{"car":car,"car_colors":car_colors,"brands":brands,"colors":colors,"FuelChoices":Car.FuelChoices.choices,"car_photos":car_photos})
    except Car.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')




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



def search_color(request):
    color_name = request.GET.get('color_name', '') 

    if color_name:
        try:
            color = Color.objects.get(name__iexact=color_name) 
            return redirect('cars:update_color_view', color_id=color.id) 
        except Color.DoesNotExist:
            messages.error(request, 'Color not found.','alert-danger')
            return redirect('main:home_view') 
    else:
        messages.error(request, 'Please enter a color name to search.','alert-danger')
        return redirect('main:home_view') 

def delete_car_view(request,car_id):
    try:
        car=Car.objects.get(pk=car_id)
        car.delete()
        messages.success(request, 'The car has been deleted successfully!','alert-success')
        return redirect("main:home_view")
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}",'alert-danger')
        return redirect('main:home_view')

def delete_color_view(request,color_id):
    try:
        color=Color.objects.get(pk=color_id)
        color.delete()
        messages.success(request, 'The color has been deleted successfully!','alert-success')
        return redirect("main:home_view")
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}",'alert-danger')
        return redirect('main:home_view')