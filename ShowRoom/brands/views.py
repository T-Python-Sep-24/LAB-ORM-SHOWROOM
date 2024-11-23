from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Brand
from .forms import BrandForm
from cars.models import Car


def all_brands(request):
    brands = Brand.objects.all()

    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        brands = brands.filter(name__icontains=search_query)

    return render(request, 'brands/all_brands.html', {'brands': brands})

def brand_detail(request: HttpRequest, brand_id: int):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = brand.cars.all()  # Cars belonging to this brand
    return render(request, 'brands/brand_detail.html', {'brand': brand, 'cars': cars})

def new_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)  # Include FILES for image uploads
        if form.is_valid():
            form.save()
            messages.success(request, "Brand added successfully!")
            return redirect('brands:all_brands')
    else:
        form = BrandForm()
    return render(request, 'brands/brand_form.html', {'form': form})

def update_brand(request: HttpRequest, brand_id: int):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand updated successfully!")
            return redirect('brands:brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brands/brand_form.html', {'form': form})

def delete_brand(request: HttpRequest, brand_id: int):
    brand = get_object_or_404(Brand, id=brand_id)
    brand.delete()
    messages.success(request, "Brand deleted successfully!")
    return redirect('brands:all_brands')
