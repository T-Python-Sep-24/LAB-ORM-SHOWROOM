from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from brands.models import Brand
from brands.forms import BrandForm
from cars.models import Car, Attachment
from django.db.models import Q, Count
from django.core.paginator import Paginator

# Add brand instance
def addBrandView(request: HttpRequest):

    if not request.user.is_staff:
        messages.warning(request, "Only staff can add brands.", "alert-warning")
        response = redirect('main:homeView')
    else:
        brandData = BrandForm()
        response = render(request, 'brands/addBrand.html')
        
        if request.method == "POST":
            brandData = BrandForm(request.POST, request.FILES)
            if brandData.is_valid():
                brandData.save()
                messages.success(request, f"'{request.POST['name']}' added successfully.", "alert-success")
            else:
                messages.error(request, f"'{request.POST['name']}' wasn't added.", "alert-danger")
                
            response = redirect('brands:displayBrandsView')
    
    return response

# Update brand instance
def updateBrandView(request: HttpRequest, brandid:int):

    if not request.user.is_staff:
        messages.warning(request, "Only staff can update brands.", "alert-warning")
        response = redirect('main:homeView')
    else:
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
                    messages.error(request, f"'{request.POST['name']}' wasn't updated.", "alert-danger")
                    
                response = redirect('brands:brandDetailsView', brandid)
    
    return response

# Delete brand view
def deleteBrandView(request:HttpRequest, brandid:int):

    if not request.user.is_staff:
        messages.warning(request, "Only staff can delete brands.", "alert-warning")
        response = redirect('main:homeView')
    else:
    
        try:
            brand = Brand.objects.get(pk=brandid)
        except Exception:
            response = render(request, '404.html')
        else:
            try:
                brand.delete()
            except Exception:
                messages.error(request, f"'{brand.name}' wasn't deleted.", "alert-danger")
            else: 
                messages.success(request, f"'{brand.name}' deleted successfully.", "alert-success")    
            
            response = redirect('brands:displayBrandsView')

    return response

# Display all brands
def displayBrandsView(request: HttpRequest):
    
    brands = Brand.objects.all().order_by('founded')
    brands = brands.annotate(carCount=Count("car"))

    if "search" in request.GET and len(request.GET["search"]) >= 2:
        brands = brands.filter(name__contains=request.GET["search"]).order_by('-founded')

    paginator = Paginator(brands, 6)
    pageNumber = request.GET.get('page', 1)
    page_obj = paginator.get_page(pageNumber)

    response = render(request, 'brands/displayBrands.html', context={'brands': page_obj})
    return response

# Brand details view
def brandDetailsView(request: HttpRequest, brandid:int):
    try:
        brand = Brand.objects.get(pk=brandid)
    except Exception:
        response = render(request, '404.html')
    else:

        brandCars = Car.objects.filter(brand=brand)[0:2]
        response = render(request, 'brands/brandDetails.html', context={'brand': brand, 'brandCars': brandCars})
        
    return response