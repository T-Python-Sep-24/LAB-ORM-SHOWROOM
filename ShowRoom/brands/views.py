from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse

from django.contrib import messages
from .models import Brand

# Create your views here.

def new_brand_view(request:HttpRequest):

    if request.method == "POST": 
        new_brand = Brand(
            name= request.POST["name"], 
            logo = request.FILES["logo"], 
            about = request.POST ["about"],
            founded_at = request.POST["founded_at"] 
        )
        new_brand.save()
    return render(request, 'brands/new_brand.html')

def all_brands_view(request:HttpRequest):
    brands = Brand.objects.all()
    return render(request, 'brands/all_brands.html', {'brands': brands})



def  brand_detail_view(request:HttpRequest, brand_id):
    
    brand = Brand.objects.get(pk=brand_id)
    return render(request, 'brands/brand_detail.html', {'brand': brand})
def update_brand_view(request:HttpRequest, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    
    if request.method == "POST":
        brand.name = request.POST.get("name")
        brand.about = request.POST.get("about")
        brand.founded_at = request.POST.get("founded_at")
        if 'logo' in request.FILES:
            brand.logo = request.FILES['logo']
        brand.save()

        return redirect('brands:brand_detail_view', brand_id=brand.id)
    return render (request , 'brands/update_brand.html  ', {"brand":brand})