from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpRequest,HttpResponse
from django.core.paginator import Paginator
from .models import Car , Color ,Review
from brands.models import Brand
# Create your views here.


def add_car_view(request: HttpRequest):
    cars = Car.objects.all()  

    if request.method == "POST":
        name = request.POST.get("name")
        brand_id = request.POST.get("brand")
        photo = request.FILES.get("photo")
        model_year = request.POST.get("model_year")
        price = request.POST.get("price")
        fuel_type = request.POST.get("fuel_type")
        new_car = Car(
            name=name,
            brand=Brand.objects.get(id=brand_id),
            photo=photo,
            model_year=int(model_year),
            price=float(price),
            fuel_type=(fuel_type == "True"),
        )
        new_car.save()
        new_car.colors.set(request.POST.getlist("colors"))  
        return redirect("cars:all_cars_view")
    return render(request, "cars/add_car.html",{"brands": Brand.objects.all(),"colors": Color.objects.all(),})

def all_cars_view(request):
    search_query = request.GET.get('search', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 9000000)
    brand_id = request.GET.get('brand', None)
    cars = Car.objects.all()

    if search_query:
        cars = cars.filter(name__icontains=search_query)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if brand_id:
        cars = cars.filter(brand_id=brand_id)

    paginator = Paginator(cars, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    brands = Brand.objects.all()
    return render(request, "cars/all_cars.html",{"cars": page_obj,"search_query": search_query,"min_price": min_price,"max_price": max_price,"brand_id": brand_id,"brands": brands})

def detail_view(request:HttpRequest, car_id:int):
    car = Car.objects.get(pk=car_id)
    reviews = Review.objects.filter(car = car)
    return render(request,"cars/detail.html",{"car":car,"reviews":reviews})

def update_view(request: HttpRequest, car_id: int):
    car_detail = get_object_or_404(Car, pk=car_id)
    if request.method == "POST":
        car_detail.name = request.POST["name"]
        car_detail.brand = request.POST["brand"]
        if "photo" in request.FILES:
            car_detail.photo = request.FILES["photo"]
        car_detail.model_year = request.POST["model_year"]
        car_detail.price = request.POST["price"]
        car_detail.fuel_type = request.POST["fuel_type"] == "True"
        car_detail.colors.set(request.POST.getlist("colors"))
        car_detail.save()
        return redirect("cars:all_cars_view")

    brands = Brand.objects.all()
    colors = Color.objects.all()
    return render(request, "cars/update.html",{"car": car_detail,"brands": brands,"colors": colors})
    
def delete_view(request:HttpRequest, car_id:int):
    car_detail = Car.objects.get(pk=car_id)
    car_detail.delete()
    return render(request,"cars/all_cars.html",{"car_detail":car_detail})



def add_color_view(request:HttpRequest):
    if request.method == "POST":
        new_color = Color(
            name=request.POST["name"],
            photo=request.FILES["photo"],
            )
        new_color.save()
        
        return redirect("cars:all_cars_view") 
    return render(request,"cars/add_color.html")


def delete_color_view(request:HttpRequest):
    return render(request,"cars/all_cars.html")


def update_color(request: HttpRequest, color_id: int):
    color = Color.objects.get(pk=color_id)

    if request.method == "POST":
        color.name = request.POST["name"]
        if "photo" in request.FILES:  
            color.photo = request.FILES["photo"]
        color.save()
        return redirect("colors:all_colors_view")
    return render(request, "colors/update_color.html", {"color": color})

def add_review_view(request:HttpRequest,car_id:int):
    car_object = Car.objects.get(pk=car_id)
    if request.method == "POST":
        car_object = Car.objects.get(pk=car_id)
        new_review = Review(car=car_object ,user=request.user,comment=request.POST["comment"])
        new_review.save()
    return redirect("cars:detail_view",car_id=car_id)