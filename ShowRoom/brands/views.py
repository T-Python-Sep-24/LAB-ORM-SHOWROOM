from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Brand
from .forms import BrandForm
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def manage_brand_view(request , brand_id = None):

    brand = None
    if brand_id:
        try:
            brand = Brand.objects.get(pk=brand_id)
        except Brand.DoesNotExist:
            pass
    elif request.method   == "POST":
        form = BrandForm(request.POST,request.FILES, instance = brand)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = BrandForm(instance=brand)
    
    return render(request, 'brands/manage_brand.html', {'form':form , 'brand':brand})

def all_brands_view(request):
    query = request.GET.get('q', '')
   
    
    if query:
        brands = Brand.objects.filter(name__icontains=query)
    else:
        brands = Brand.objects.all()
    
    paginator = Paginator(brands, 1)  
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
