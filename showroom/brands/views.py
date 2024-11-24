from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand
from .forms import BrandForm
from django.contrib import messages

def all_brands(request):
    brands = Brand.objects.all()
    return render(request, 'brands/all_brands.html', {'brands': brands})


def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brands/brand_detail.html', {'brand': brand})


def new_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brands:all_brands')
    else:
        form = BrandForm()
    return render(request, 'brands/new_brand.html', {'form': form})


def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brands:brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)

    return render(request, 'brands/update_brand.html', {'form': form, 'brand': brand})


def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, "Brand deleted successfully!")
        return redirect('brands:all_brands')
    return render(request, 'brands/delete_brand.html', {'brand': brand})

