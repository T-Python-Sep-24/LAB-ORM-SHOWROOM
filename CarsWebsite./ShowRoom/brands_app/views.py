from django.shortcuts import render,redirect , get_object_or_404
from .models import Brand
from django.http import HttpRequest , HttpResponse
from .form import BrandForm
from django.contrib import messages


def all_brands_view(request:HttpRequest):
    brands = Brand.objects.all()  
    return render(request, 'brands_app/all_brands.html', {'brands': brands})
  
 

def brand_detail_view(request:HttpRequest,brand_id):
    brand = get_object_or_404(Brand, id=brand_id) 
    return render(request, 'brands_app/brand_detail.html', {'brand': brand})
 


def new_brand_view(request: HttpRequest):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            messages.success(request, "Brand created successfully!")
        return redirect('brands_app:all_brands_view') 
    else:

      form = BrandForm()  

    return render(request, 'brands_app/add_new_brand.html', {'form': form})  


def update_brand_view(request:HttpRequest , brand_id):
    brand = get_object_or_404(Brand, id=brand_id)  
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)  
        if form.is_valid():
            form.save()  # Save the updated brand
            messages.success(request, "Brand updated successfully!")
            return redirect('brand_detail_view', brand_id=brand.id) 
    else:
        form = BrandForm(instance=brand) 

    return render(request, 'brands_app/update_brand.html', {'form': form})


def brand_delete_view(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)  
    if request.method == 'POST':
        brand.delete() 
        messages.success(request, "Brand deleted successfully!")
        return redirect('brand_list')  
    return render(request, 'brands_app/delete_brand.html', {'brand': brand})  

 




