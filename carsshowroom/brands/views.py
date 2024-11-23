from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from .models import Brand
from .forms import BrandForm
# Create your views here.
from django.apps import apps



def all_brands_view(request:HttpRequest):
    brands=Brand.objects.all()
    if "search" in request.GET :
        brands = Brand.objects.filter(name__contains=request.GET["search"])
    brands= brands.annotate(car_count=Count('cars'))
    page_number = request.GET.get("page", 1)
    
    paginator = Paginator(brands, 8)
    brand_page = paginator.get_page(page_number)
    return render(request,"brands/all_brands.html",context={"brands":brand_page})

def new_brand_view(request:HttpRequest):

    brand_form=BrandForm()

    if request.method =='POST':
        brand_form=BrandForm(request.POST,request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request,"brand has been added successfully ","alert-success")
            return redirect("brands:all_brands_view")
        else:
            messages.error(request,brand_form.errors,"alert-danger")
    return render(request,"brands/new_brand.html",context={'brand_form':brand_form,})

def brand_detail_view(request:HttpRequest,brand_id:int):
    brand=Brand.objects.get(pk=brand_id)

    cars=brand.cars.all()
     
    return render(request,"brands/brand_detail.html",{"brand":brand,"cars":cars})

def brand_update_view(request:HttpRequest,brand_id:int):
    
    brand=Brand.objects.get(pk=brand_id)
   
    if request.method =='POST':
        brand_form=BrandForm(instance=brand,data=request.POST,files=request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request,"brand has been updated successfully ","alert-success")
            return redirect("brands:brand_detail_view", brand_id=brand.id)
        else:
            messages.error(request,brand_form.errors,"alert-danger")
    return render(request,"brands/update_brand.html",context={'brand':brand})


def delete_brand_view(request:HttpRequest,brand_id:int):
    try:
        brand=Brand.objects.get(pk=brand_id)
        brand.delete()
        messages.success(request, f"Deleted {brand.name} successfully", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, f"Couldn't Delete {brand.name} ", "alert-danger")
    return redirect ("brands:all_brands_view")
