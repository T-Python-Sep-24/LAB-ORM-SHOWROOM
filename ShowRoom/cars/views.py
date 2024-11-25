from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Car, Color
from .forms import CarForm, ColorForm
from brands.models import Brand
from django.core.paginator import Paginator




def all_cars(request):
    cars = Car.objects.all()  # Fetch all cars
    brands = Brand.objects.all()  # Fetch all brands for the filter
    colors = Color.objects.all()  # Fetch all colors for the filter

    # Filters and search
    brand_filter = request.GET.get('brand', '')
    color_filter = request.GET.get('color', '')
    year_filter = request.GET.get('year', '')
    search_query = request.GET.get('search', '')

    # Apply filters
    if brand_filter:
        cars = cars.filter(brand__id=brand_filter)
    if color_filter:
        cars = cars.filter(colors__id=color_filter)
    if year_filter:
        cars = cars.filter(year=year_filter)
    if search_query:
        cars = cars.filter(name__icontains=search_query)

    # Get unique years for dropdown
    years = Car.objects.values_list('year', flat=True).distinct().order_by('year')

    # Pagination setup
    paginator = Paginator(cars, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cars/all_cars.html', {
        'cars': page_obj,
        'brands': brands,
        'colors': colors,
        'years': years,
        'paginator': paginator,
        'page_obj': page_obj,
    })


def car_detail(request: HttpRequest, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def new_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect('cars:all_cars')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

def update_car(request: HttpRequest, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect('cars:car_detail', car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form})

def delete_car(request: HttpRequest, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    messages.success(request, "Car deleted successfully!")
    return redirect('cars:all_cars')

def new_color(request: HttpRequest):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Color added successfully!")
            return redirect('cars:all_cars')
    else:
        form = ColorForm()
    return render(request, 'cars/color_form.html', {'form': form})

def update_color(request: HttpRequest, color_id: int):
    color = get_object_or_404(Color, id=color_id)
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, "Color updated successfully!")
            return redirect('cars:all_cars')
    else:
        form = ColorForm(instance=color)
    return render(request, 'cars/color_form.html', {'form': form})
