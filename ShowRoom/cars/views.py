from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Color , Brand , Review
from .forms import CarForm  , ColorForm , ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

def is_admin(user):
    return user.is_superuser

def all_cars(request):
    cars = Car.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()


    brand_filter = request.GET.get('brand', None)
    color_filter = request.GET.get('color', None)
    search = request.GET.get('search', '')

    if brand_filter:
        cars = cars.filter(brand__id=brand_filter)
    if color_filter:
        cars = cars.filter(colors__id=color_filter)
    if search:
        cars = cars.filter(name__icontains=search)

    paginator = Paginator(cars, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    no_results = cars.count() == 0
    
    return render(
        request,
        'cars/all_cars.html',
        {
            'cars': page_obj,
            'colors': colors,
            'brands': brands,
            'brand_filter': brand_filter,
            'color_filter': color_filter,
            'search': search,
            'no_results': no_results
        }
    )

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    reviews = car.reviews.all()

    form = ReviewForm()

    for review in reviews:
        review.full_stars = [1] * review.rating 
        review.empty_stars = [1] * (5 - review.rating)

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.car = car
            review.save()
            return redirect('cars:car_detail', car_id=car.id)  

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'reviews': reviews,
        'form': form,
        'is_authenticated': request.user.is_authenticated  
    })

@user_passes_test(is_admin)
def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        
        if form.is_valid():
            car = form.save(commit=False) 
            car.save() 
            form.save_m2m() 
            messages.success(request, 'Car added successfully!')
            return redirect('cars:all_cars')
        else:
            messages.error(request, 'There were some errors with your form.')
            print(form.errors)  
    else:
        form = CarForm()

    return render(request, 'cars/new_car.html', {'form': form})

@user_passes_test(is_admin)
def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('cars:car_detail', car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/update_car.html', {'form': form, 'car': car})

@user_passes_test(is_admin)
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        car.delete()
        messages.success(request, f"Car '{car.name}' has been successfully deleted!")
        return redirect('cars:all_cars') 
    
    return render(request, 'cars/delete_car.html', {'car': car})

@user_passes_test(is_admin)
def add_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Color added successfully!')
            return redirect('cars:all_colors')  
    else:
        form = ColorForm()
    return render(request, 'cars/add_color.html', {'form': form})

@user_passes_test(is_admin)
def all_colors(request):
    colors = Color.objects.all()
    return render(request, 'cars/all_colors.html', {'colors': colors})


@user_passes_test(is_admin)
def update_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, "Color updated successfully!")
            return redirect('cars:all_colors') 
    else:
        form = ColorForm(instance=color)

    return render(request, 'cars/update_color.html', {'form': form})

@user_passes_test(is_admin)
def delete_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    
    if request.method == 'POST':
        color.delete()
        messages.success(request, f"Color '{color.name}' has been successfully deleted!")
        return redirect('cars:all_colors')  
    
    return render(request, 'cars/delete_color.html', {'color': color})


@user_passes_test(is_admin)
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if not request.user.is_superuser:
        raise Http404("You do not have permission to delete this review.")
    
    review.delete()
    messages.success(request, "Review deleted successfully!")

    return redirect('cars:car_detail', car_id=review.car.id)
