from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Count
from django.contrib import messages
from .models import Brand
from cars.models import Car 
from .forms import BrandForm


# Create your views here.


def all_brands(request):
    query = request.GET.get('q', '')  
    brands = Brand.objects.annotate(car_count=Count('cars'))  
    if query:
        brands = brands.filter(name__icontains=query)
    return render(request, 'all_brands.html', {'brands': brands, 'query': query})


def brand_details(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = Car.objects.filter(brand=brand)  
    return render(request, 'brands_details.html', {'brand': brand, 'cars': cars})



def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand added successfully!")
            return redirect('all_brands')
    else:
        form = BrandForm()
    
    brands = Brand.objects.all()  
    return render(request, 'add_brand.html', {'form': form, 'brands': brands})


def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, f"The brand '{brand.name}' has been updated successfully!")
            return redirect('all_brands')  
    else:
        form = BrandForm(instance=brand)

    return render(request, 'update_brand.html', {'form': form, 'brand': brand})


def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == "POST":
        brand_name = brand.name  
        brand.delete()
        messages.error(request, f"The brand '{brand_name}' has been deleted successfully!")
        return redirect('all_brands') 
    return redirect('add_brand')