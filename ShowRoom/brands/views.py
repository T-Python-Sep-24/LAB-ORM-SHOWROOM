from django.shortcuts import render
from .models import Brand

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brand_list.html', {'brands': brands})

def brand_detail(request, brand_id):
    try:
        brand = Brand.objects.get(pk=brand_id)
    except Brand.DoesNotExist:
        brand = None

    if brand is None:
        return render(request, 'brands/brand_not_found.html', status=404)
    
    return render(request, 'brands/brand_detail.html', {'brand': brand})
