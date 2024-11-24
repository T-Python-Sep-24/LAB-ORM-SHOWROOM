from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Brand
from .forms import BrandForm
from cars.models import Car



def all_brands(request):
    search_query = request.GET.get('search', '')
    founded_at_filter = request.GET.get('founded_at', '')
    headquarters_filter = request.GET.get('headquarters', '')

    brands = Brand.objects.all()

    if search_query:
        brands = brands.filter(name__icontains=search_query)
    if founded_at_filter:
        brands = brands.filter(founded_at=founded_at_filter)
    if headquarters_filter:
        brands = brands.filter(headquarters__icontains=headquarters_filter)

    years = Brand.objects.values_list('founded_at', flat=True).distinct()
    headquarters = Brand.objects.values_list('headquarters', flat=True).distinct()

    return render(request, 'brands/all_brands.html', {
        'brands': brands,
        'years': years,
        'headquarters': headquarters,
    })


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
