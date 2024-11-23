from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from .models import Brand
from .forms import BrandForm
from django.contrib import messages

# Create your views here.
def all_brands(request):
    query = request.GET.get('q', '')  # Search query
    sort = request.GET.get('sort', '')  # Sorting parameter
    brands = Brand.objects.all()

    # Filter by search query
    if query:
        brands = brands.filter(name__icontains=query)

    # Sort by name or number of cars
    if sort == 'name':
        brands = brands.order_by('name')
    elif sort == 'cars':
        brands = sorted(brands, key=lambda b: b.cars.count(), reverse=True)


    # Paginate the results
    paginator = Paginator(brands, 6)  # 6 brands per page
    page_number = request.GET.get('page')
    brands = paginator.get_page(page_number)

    return render(request, 'brand/all_brands.html', {'brands': brands, 'query': query, 'sort': sort})

def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand has been successfully created!")
            return redirect('brands:all_brands')
        else:
            messages.error(request, "Error creating brand. Please check the form.")
    else:
        form = BrandForm()
    return render(request, 'brand/create_brand.html', {'form': form})


def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = brand.cars.all()  # Fetch cars related to the brand
    return render(request, 'brand/brand_detail.html', {'brand': brand, 'cars': cars})

def brand_update(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, f"Brand '{brand.name}' has been successfully updated!")
            return redirect('brands:brand_detail', brand_id=brand.id)
        else:
            messages.error(request, "Error updating brand. Please check the form.")
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brand/brand_update.html', {'form': form, 'brand': brand})


def brand_delete(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, f"Brand '{brand.name}' has been successfully deleted!")
        return redirect('brands:all_brands')
    return render(request, 'brand/brand_delete.html', {'brand': brand})
