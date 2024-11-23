from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Brand
from .forms import BrandForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def manage_brand_view(request, brand_id=None):
    brand = None

    if brand_id:
        try:
            brand = Brand.objects.get(pk=brand_id)
        except Brand.DoesNotExist:
            messages.error(request, "The brand you are trying to edit does not exist.")
            return redirect('brands:all_brands_view')

    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES, instance=brand)
        
        if form.is_valid():
            form.save()

            if not brand_id:
                messages.success(request, "Brand added successfully.")
            else:
                messages.success(request, "Brand updated successfully.")

            return redirect('brands:all_brands_view')

    else:
        form = BrandForm(instance=brand)

    return render(request, 'brands/manage_brand.html', {'form': form, 'brand': brand})

def delete_brand(request, brand_id):
    try:
        brand = Brand.objects.get(pk=brand_id)
        brand.delete()
        messages.success(request, "Brand deleted successfully.")
    except Brand.DoesNotExist:
        messages.error(request, "The brand you are trying to delete does not exist.")
    return redirect('brands:all_brands_view')

def all_brands_view(request):
    query = request.GET.get('q', '')
   
    
    if query:
        brands = Brand.objects.filter(name__icontains=query)
    else:
        brands = Brand.objects.all()
    
    paginator = Paginator(brands, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    return render(request, 'brands/brands.html', {'page_obj': page_obj, 'query': query})


def brand_details_view(request , brand_id = None):
     
    try:
        brand = Brand.objects.get(pk=brand_id)

        cars = brand.cars.all().order_by('-id')[:3]

    except Brand.DoesNotExist:
          return redirect('brands:all_brands') 
    
    return render(request, 'brands/details.html', {'brand': brand , 'cars':cars})
