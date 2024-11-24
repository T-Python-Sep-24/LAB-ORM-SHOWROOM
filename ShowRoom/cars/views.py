from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse

from django.contrib import messages
from . models import Car , Color
from brands .models import Brand
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def all_cars_view(request:HttpRequest):
    filters = Q()

    search_query = request.GET.get("search", "").strip()
    brand_filter = request.GET.get("brand", "").strip()
    color_filter = request.GET.get("color", "").strip()

    if search_query:
        filters &= Q(name__icontains=search_query)
    if brand_filter:
        filters &= Q(brand__name__iexact=brand_filter)  
    if color_filter:
        filters &= Q(colors__name__iexact=color_filter)  
    
    cars = Car.objects.filter(filters).distinct()
    
    paginator = Paginator(cars, 10)  
    page_number = request.GET.get("page")
    page_cars = paginator.get_page(page_number)

    
    brands = Brand.objects.all()
    colors = Color.objects.values("name").distinct()  
    
    return render(request, "cars/all_cars.html", {
        "cars": page_cars,
        "brands": brands,
        "colors": colors,
        "search_query": search_query,
        "selected_brand": brand_filter,
        "selected_color": color_filter,
    })

def new_car_view(request:HttpRequest):
    
    if request.method == "POST":
        color_name = request.POST.get("color", "").strip()
        
        color, created = Color.objects.get_or_create(name=color_name)    
        
        brand = Brand.objects.get(name=request.POST["brand"].strip())
        new_car = Car(
            name=request.POST["name"],
            brand=brand,
            photo=request.FILES["photo"],
            specs=request.POST["specs"],
            model_year=request.POST["model_year"],
        )
        new_car.save()
        
        new_car.colors.add(color)  
        messages.success(request, f"Car '{new_car.name}' has been successfully created!")
        return redirect('cars:new_car_view')  

    return render(request, 'cars/new_car.html')

def update_car_view(request: HttpRequest, car_id):
    car = Car.objects.get(pk=car_id)  
    if request.method == "POST":
        
        car.name = request.POST.get("name")
        car.specs = request.POST.get("specs")
        car.model_year = request.POST.get("model_year")
        
        brand_name = request.POST.get("brand")
        brand, created = Brand.objects.get_or_create(name=brand_name.strip())
        car.brand = brand

        
        color_name = request.POST.get("colors").strip()
        color = Color.objects.filter(name=color_name).first()  
        if not color:
            color = Color.objects.create(name=color_name)  
        car.colors.set([color]) 

        
        if 'photo' in request.FILES:
            car.photo = request.FILES['photo']
        
        car.save()
        messages.success(request, f"Car '{car.name}' has been successfully updated!")
        return redirect('cars:all_cars_view')  

    return render(request, 'cars/update_car.html', {'car': car})
        

def details_car_view(request, car_id):
    
    car = Car.objects.get(pk=car_id)
    
    return render(request, 'cars/car_detail.html', {'car': car})


def new_color_view(request: HttpRequest):
    color_name = request.POST.get("name", "").strip()
    hex_value = request.POST.get("hex_value", "").strip()
                
    color, created = Color.objects.get_or_create(name__iexact=color_name, defaults={"hex_value": hex_value})
    if not created:
        color.hex_value = hex_value
        color.save()

        messages.success(request, f"Color '{color.name}' has been added or updated.")
        return redirect('cars:new_color_view')  

    return render(request, 'cars/new_color.html')


def update_color_view(request: HttpRequest, color_id):
    
    color = Color.objects.get(pk=color_id)

    if request.method == "POST":
        color.name = request.POST["name"]
        color.hex_value = request.POST["hex_value"]
        color.save()
        messages.success(request, f"Color '{color.name}' has been successfully updated!")
        return redirect('cars:update_color', color_id=color.id)  

    return render(request, 'cars/update_color.html', {'color': color})