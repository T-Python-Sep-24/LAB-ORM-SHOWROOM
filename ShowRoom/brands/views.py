from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Brand
from .forms import BrandForm

def all_brands(request):
    brands = Brand.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        brands = brands.filter(name__icontains=search_query)
    return render(request, 'brands/all_brands.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brands/brand_detail.html', {'brand': brand})

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_superuser)
def new_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand added successfully!')
            return redirect('brands:all_brands')
    else:
        form = BrandForm()
    return render(request, 'brands/new_brand.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser)
def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand updated successfully!')
            return redirect('brands:brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brands/update_brand.html', {'form': form, 'brand': brand})

@user_passes_test(lambda user: user.is_superuser)
def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'Brand deleted successfully!')
        return redirect('brands:all_brands')
    return render(request, 'brands/delete_brand.html', {'brand': brand})
