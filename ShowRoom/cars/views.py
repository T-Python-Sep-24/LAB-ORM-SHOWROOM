from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Color, Photo, Review
from brands.models import Brand
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .forms import ColorForm, CarForm, PhotoForm

# Create your views here.


def all_cars(request):
    cars = Car.objects.all()
    
    query = request.GET.get('q')
    brand_filter = request.GET.get('brand')
    color_filter = request.GET.get('color')

    if query:
        cars = cars.filter(name__icontains=query)
    if brand_filter:
        cars = cars.filter(brand__id=brand_filter)
    if color_filter:
        cars = cars.filter(colors__id=color_filter)
    
    paginator = Paginator(cars, 10)
    page = request.GET.get('page')
    paginated_cars = paginator.get_page(page)


    brands = Brand.objects.all()
    colors = Color.objects.all()
    
    return render(request, 'all_cars.html', {
        'cars': paginated_cars,
        'brands': brands,
        'colors': colors,
        'page_obj': paginated_cars,  
    })


def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)  
    photos = car.photos.all()  
    return render(request, 'car_details.html', {'car': car, 'photos': photos})



def add_car(request):
    if not request.user.is_staff:
        messages.error(request, "only staff can edit")
        return redirect("home")
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            for img_file in request.FILES.getlist('photos'):
                Photo.objects.create(car=car, photo=img_file)

            messages.success(request, "Car added successfully!")
            return redirect('all_cars')
    else:
        form = CarForm()

    brands = Brand.objects.all()
    colors = Color.objects.all()

    return render(request, 'add_car.html', {
        'form': form,
        'brands': brands,
        'colors': colors,
    })



def update_car(request, car_id):
    if not request.user.is_staff:
        messages.error(request, "only staff can edit")
        return redirect("home")
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save()
            for img_file in request.FILES.getlist('photos'):
                Photo.objects.create(car=car, photo=img_file)

            messages.success(request, "Car updated successfully!")
            return redirect('car_details', car_id=car.id)
    else:
        form = CarForm(instance=car)

    brands = Brand.objects.all()
    colors = Color.objects.all()

    return render(request, 'update_car.html', {
        'form': form,
        'car': car,
        'brands': brands,
        'colors': colors,
    })



def delete_car(request, car_id):
    if not request.user.is_staff:
        messages.error(request, "only staff can edit")
        return redirect("home")
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        car.delete()
        messages.error(request, f"The car '{car.name}' has been deleted.")
        return redirect('all_cars')  
    return redirect('car_detail', id=car_id)

def add_color(request):
    if not request.user.is_staff:
        messages.error(request, "only staff can edit")
        return redirect("home")
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            color = form.save()
            messages.success(request, f"The color '{color.name}' has been successfully added.")
    else:
        form = ColorForm()
    return render(request, 'add_color.html', {'form': form})

def update_color(request, color_id):
    if not request.user.is_staff:
        messages.error(request, "only staff can edit")
        return redirect("home")
    color = get_object_or_404(Color, id=color_id)
    if request.method == "POST":
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, f"The color '{color.name}' has been successfully updated.")
    else:
        form = ColorForm(instance=color)
    return render(request, 'update_color.html', {'form': form, 'color': color})


def delete_color(request, color_id):
    if not request.user.is_staff:
        messages.error(request, "only staff can edit")
        return redirect("home")
    color = get_object_or_404(Color, id=color_id)
    if request.method == "POST":
        color_name = color.name 
        color.delete()
        messages.error(request, f"The color '{color_name}' has been deleted successfully!")
        return redirect('add_color')  
    messages.error(request, "Invalid request to delete the color.")
    return redirect('add_color')



def add_review(request, car_id: int):
    if not request.user.is_authenticated:
        messages.error(request, "Only registered users can add reviews")
        return redirect("accounts:sign_in")

    if request.method == "POST":
        car_object = get_object_or_404(Car, pk=car_id)  
        new_review = Review(
            car=car_object,
            user=request.user,
            comment=request.POST["comment"],
            rating=request.POST["rating"]
        )
        new_review.save()

        messages.success(request, "Review added successfully!")
    return redirect("car_details", car_id=car_id)