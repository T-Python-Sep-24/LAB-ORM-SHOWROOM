from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand
from .forms import BrandForm  
from django.core.paginator import Paginator

def all_brands(request):
    brands = Brand.objects.all()
    
    
    brand_filter = request.GET.get('brand', None)
    search = request.GET.get('search', '')

    
    if brand_filter:
        brands = brands.filter(id=brand_filter)
    if search:
        brands = brands.filter(name__icontains=search)

   
    paginator = Paginator(brands, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'brands/all_brands.html', {
        'page_obj': page_obj,
        'brand_filter': brand_filter,
        'search': search,
    })

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brands/brand_details.html', {'brand': brand})

def new_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, 'The brand has been added successfully!')
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
            messages.success(request, f"Brand '{brand.name}' has been successfully updated!")
            return redirect('brands:brand_detail', brand_id=brand.id)  
    else:
        form = BrandForm(instance=brand)  

    return render(request, 'brands/update_brand.html', {'form': form, 'brand': brand})

def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, f"Brand '{brand.name}' has been successfully deleted!")
        return redirect('brands:all_brands')  
    
    return render(request, 'brands/delete_brand.html', {'brand': brand})