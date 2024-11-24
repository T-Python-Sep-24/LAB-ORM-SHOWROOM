from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .forms import CarForm , ColorForm
from .models import Car , VehiclePhoto , Color
from brands.models import Brand
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test , login_required

# Create your views here.

def admin_only(user):

    return user.is_superuser

@login_required
@user_passes_test(admin_only)
def manage_car_view(request, car_id=None):
    car = None
    if car_id:
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            messages.error(request, "The car you are trying to edit does not exist.")
            return redirect('cars:all_cars_view')

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)

        color_ids = request.POST.getlist('color')
        
        photo_files = request.FILES.getlist('image')  
        
        if form.is_valid():
            car = form.save()  

            car.color.set(color_ids) 

            for photo in photo_files:
                VehiclePhoto.objects.create(car=car, image=photo)

            if not car_id:
                messages.success(request, "Car added successfully.") 
            else:
                messages.success(request, "Car details updated successfully.") 

            return redirect('cars:all_cars_view')
    else:
        form = CarForm(instance=car)

    return render(request, 'cars/manage_car.html',locals())

@login_required
@user_passes_test(admin_only)
def delete_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        car.delete()
        messages.success(request, "Car deleted successfully.")
    except Car.DoesNotExist:
        messages.error(request, "The car you are trying to delete does not exist.")
    return redirect('cars:all_cars_view')

@login_required
@user_passes_test(admin_only)
def manage_color_view(request, color_id=None):
    color = None
    if color_id:
        try:
            color = Color.objects.get(pk=color_id)
        except Color.DoesNotExist:
            pass

    if request.method == "POST":
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            color = form.save()
            if color_id:
                messages.success(request, "Color updated successfully.")
            else:
                messages.success(request, "Color added successfully.")
                
            return redirect('cars:all_cars_view')
    else:
        form = ColorForm(instance=color)
    try:
        get_template('cars/colors/manage_color.html')
    except Exception as e:
        print(f"Error loading template: {e}")

    return render(request, 'cars/colors/manage_color.html', {'form': form, 'color': color})

@login_required
@user_passes_test(admin_only)
def delete_color(request, color_id):
    try:
        color = Color.objects.get(pk=color_id)
        color.delete()
        messages.success(request, "Color deleted successfully.")
    except Color.DoesNotExist:
        messages.error(request, "The color you are trying to delete does not exist.")
    return redirect('cars:all_cars_view')

def all_cars_view(request):
    query = request.GET.get('q', '')
    brand_filter = request.GET.get('brand', '')
    color_filter = request.GET.get('color', '')

    filter_conditions = Q()

    if query:
        filter_conditions &= Q(name__icontains=query)
    if brand_filter:
        filter_conditions &= Q(brand__name__icontains=brand_filter)
    if color_filter:
        filter_conditions &= Q(color__name__icontains=color_filter)

    cars = Car.objects.filter(filter_conditions).distinct()

    colors = Color.objects.all()
    brands = Brand.objects.all()

    paginator = Paginator(cars, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cars/all_cars.html',locals())



def car_details_view(request, card_id=None):
    try:
        car = Car.objects.get(pk=card_id)
    except Car.DoesNotExist:

        return redirect('cars:all_cars_view')
    
    return render(request, 'cars/car_details.html', {'car': car})