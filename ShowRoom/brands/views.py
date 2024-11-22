from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from brands.models import Brand
from brands.forms import BrandForm

# Add brand instance
def addBrandView(request: HttpRequest):
    
    brandData = BrandForm()
    response = render(request, 'brands/addBrand.html')
    
    if request.method == "POST":
        brandData = BrandForm(request.POST, request.FILES)
        if brandData.is_valid():
            brandData.save()
            messages.success(request, f"'{request.POST['name']}' added successfully.", "alert-success")
        else:
            messages.error(request, f"'{request.POST['name']}' wasn't added. {brandData.errors}", "alert-danger")
            
        response = redirect('main:homeView')
    
    return response

# Update brand instance
def updateBrandView(request: HttpRequest, brandid:int):
    try:
        brand = Brand.objects.get(pk=brandid)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'brands/updateBrand.html', context={'brand': brand})
        
        if request.method == "POST":
            brandData = BrandForm(request.POST, request.FILES, instance=brand)
            if brandData.is_valid():
                brandData.save()
                messages.success(request, f"'{request.POST['name']}' updated successfully.", "alert-success")
            else:
                messages.error(request, f"'{request.POST['name']}' wasn't updated. {brandData.errors}", "alert-danger")
                
            response = redirect('main:homeView')
    
    return response

# Display all brands
def displayBrandsView(request: HttpRequest):
    
    brands = Brand.objects.all().order_by('founded')
    
    response = render(request, 'brands/displayBrands.html', context={'brands': brands})
    return response
