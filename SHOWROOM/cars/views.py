from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Car, Color
from brands.models import Brand
from django.contrib import messages




# Create your views here.

def all_cars_view(request:HttpRequest):

    cars = Car.objects.all()
    return render(request, "cars/all_cars.html", {"cars": cars})




def add_new_car_view(request:HttpRequest):

    if request.method == "POST":
        car_name = request.POST.get("car_name")
        brand_id = request.POST.get("brand")
        available_colors = request.POST.getlist("available_colors")
        year = request.POST.get("year")
        engine = request.POST.get("engine")
        power = request.POST.get("power")
        price = request.POST.get("price")
        availability = request.POST.get("availability")
        speed = request.POST.get("speed")
        image = request.FILES.get("image")

        brand = get_object_or_404(Brand, id=brand_id)
        
        car = Car.objects.create(
            car_name=car_name,
            year=year,
            engine=engine,
            power=power,
            price=price,
            availability=availability,
            speed=speed,
            image=image
            )

        for color_id in available_colors:
            color = Color.objects.get(id=color_id)
            car.available_colors.add(color)


        messages.success(request, "Car successfully added!")

        return redirect("cars:car_details_view", car_id=car.id)
    
    colors = Color.objects.all()
    brands = Brand.objects.all()


    return render(request, 'cars/add_new_car.html', {"colors": colors, "brands": brands})




def car_details_view(request:HttpRequest, car_id: int):
    
    car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/car_details.html", {"car": car})



def car_update_view(request:HttpRequest):

    return render(request, 'cars/update_car.html')




def car_delete_view(request:HttpRequest):

    return render(request, 'cars/car_delete.html')

