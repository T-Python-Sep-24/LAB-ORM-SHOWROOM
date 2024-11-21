from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Brand
from .forms import BrandForm
from django.db.models import Q

# Create your views here.

def manage_brand_view(request , brand_id = None):

    brand = None
    if brand_id:
        try:
            brand = Brand.objects.get(pk=brand_id)
        except Brand.DoesNotExist:
            pass
    if request.method   == "POST":
        form = BrandForm(request.POST,request.FILES, instance = brand)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = BrandForm(instance=brand)
    
    return render(request, 'brands/manage_brand.html', {'form':form , 'brand':brand})

def all_brands_view(request):
         query = request.GET.get('q','')

         if query:
              brands = Brand.objects.filter(Q(name__icontains=query))
         else:
              brands = Brand.objects.all()
        
         return render(request, 'brands/brands.html', {'brands': brands, 'query': query})

