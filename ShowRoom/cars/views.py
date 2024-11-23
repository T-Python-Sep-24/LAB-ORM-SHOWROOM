from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
from .models import Car, Color
from brands.models import Brand
from .forms import CarForm
from django.contrib import messages

def all_cars(request):
    query = request.GET.get('q', '')  # Search query
    brand_filter = request.GET.get('brand', '')  # Filter by brand
    color_filter = request.GET.get('color', '')  # Filter by color

    cars = Car.objects.all()

    # Filter by search query
    if query:
        cars = cars.filter(name__icontains=query)

    # Filter by brand
    if brand_filter:
        cars = cars.filter(brand__id=brand_filter)

    # Filter by color
    if color_filter:
        cars = cars.filter(colors__id=color_filter)

    # Paginate results
    paginator = Paginator(cars, 10)  # 10 cars per page
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)

    brands = Brand.objects.all()
    colors = Color.objects.all()

    return render(request, 'cars/all_cars.html', {
        'cars': cars,
        'brands': brands,
        'colors': colors,
        'query': query,
        'brand_filter': brand_filter,
        'color_filter': color_filter,
    })
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car has been successfully added!")
            return redirect('cars:all_cars')
        else:
            messages.error(request, "Error adding car. Please check the form.")
    else:
        form = CarForm()
    return render(request, 'cars/create_car.html', {'form': form})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})


def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car has been successfully updated!")
            return redirect('cars:car_detail', car_id=car.id)
        else:
            messages.error(request, "Error updating car. Please check the form.")
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/update_car.html', {'form': form, 'car': car})


def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car_name = car.name
        car.delete()
        messages.success(request, f"Car '{car_name}' has been successfully deleted!")
        return redirect('cars:all_cars')
    return render(request, 'cars/delete_car.html', {'car': car})