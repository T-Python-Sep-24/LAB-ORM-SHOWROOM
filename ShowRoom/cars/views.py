from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Car, Review, Color
from .forms import CarForm, ReviewForm
from django.contrib.auth.decorators import login_required, user_passes_test
from brands.models import Brand


def all_cars(request):
    cars = Car.objects.all()
    brand_filter = request.GET.get('brand')
    color_filter = request.GET.get('color')
    search_query = request.GET.get('search', '')

    if brand_filter:
        cars = cars.filter(brand__id=brand_filter)
    if color_filter:
        cars = cars.filter(colors__id=color_filter)
    if search_query:
        cars = cars.filter(name__icontains=search_query)

    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    brands = Brand.objects.all()
    colors = Color.objects.all()

    return render(request, 'cars/all_cars.html', {
        'page_obj': page_obj,
        'brands': brands,
        'colors': colors,
        'brand_filter': brand_filter,
        'color_filter': color_filter,
        'search': search_query,
    })


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    reviews = car.reviews.all()
    return render(request, 'cars/car_detail.html', {'car': car, 'reviews': reviews})


@user_passes_test(lambda user: user.is_superuser)
def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect('cars:all_cars')
    else:
        form = CarForm()
    return render(request, 'cars/new_car.html', {'form': form})


@user_passes_test(lambda user: user.is_superuser)
def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    brands = Brand.objects.all()
    colors = Color.objects.all()
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect('cars:car_detail', car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/update_car.html', {'form': form, 'brands': brands, 'colors': colors})


@user_passes_test(lambda user: user.is_superuser)
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car deleted successfully!')
        return redirect('cars:all_cars')
    return render(request, 'cars/delete_car.html', {'car': car})


def new_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Color added successfully!')
            return redirect('cars:all_cars')
    else:
        form = ColorForm()
    return render(request, 'cars/new_color.html', {'form': form})


def update_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, 'Color updated successfully!')
            return redirect('cars:all_cars')
    else:
        form = ColorForm(instance=color)
    return render(request, 'cars/update_color.html', {'form': form})


def delete_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    if request.method == 'POST':
        color.delete()
        messages.success(request, 'Color deleted successfully!')
        return redirect('cars:all_cars')
    return render(request, 'cars/delete_color.html', {'color': color})


@login_required
def submit_review(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if Review.objects.filter(user=request.user, car=car).exists():
        messages.info(request, "You've already reviewed this car!")
        return redirect('cars:car_detail', car_id=car.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.car = car
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been submitted!")
            return redirect('cars:car_detail', car_id=car.id)
        else:
            messages.error(request, "There was an error submitting your review. Please check the form.")
    else:
        form = ReviewForm()

    return render(request, 'cars/submit_review.html', {'form': form, 'car': car})
