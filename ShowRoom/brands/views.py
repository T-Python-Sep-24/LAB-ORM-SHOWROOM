from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import BrandForm
from .models import Brand
from cars.models import Car
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def all_brands_view(request:HttpRequest):
    brands=Brand.objects.all()
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        brands = brands.filter(name__icontains=request.GET["search"])

    p=Paginator(brands,3)
    page=request.GET.get('page',1)
    brands_list=p.get_page(page)
    return render(request,'brands/all_brands.html',{"brands":brands_list})

def new_brand_view(request:HttpRequest):
    if not request.user.is_superuser:
            messages.warning(request,"only staff can add brand","alert-warning")
            return redirect("main:home_view")
    if request.method=="POST":
        brand_form=BrandForm(request.POST,request.FILES)
        if brand_form.is_valid():
                brand_form.save()
                messages.success(request, 'The brand has been added successfully!','alert-success')
                return redirect("brands:new_brand_view")
        else:
            print("form is not valid")
            print(brand_form.errors)
    return render(request,'brands/new_brand.html')

def update_brand_view(request:HttpRequest,brand_id):
    try:
        if not request.user.is_superuser:
            messages.warning(request,"only staff can update brand","alert-warning")
            return redirect("main:home_view")
        brand=Brand.objects.get(pk=brand_id)
        if request.method=="POST":
            brand_form=BrandForm(request.POST,request.FILES,instance=brand)
            if brand_form.is_valid():
                brand_form.save()
                messages.success(request, 'The brand has been updated successfully!','alert-success')
                return redirect('brands:update_brand_view',brand_id=brand.id)
            else:
                print("form is not valid")
                print(brand_form.errors)
                return redirect('main:home_view') 
        else:   
            brand_form = BrandForm(instance=brand)
        return render(request,'brands/update_brand.html',{"brand":brand})

    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')

def delete_brand_view(request:HttpRequest,brand_id):
    try:
        if not request.user.is_superuser:
            messages.warning(request,"only staff can delete brand","alert-warning")
            return redirect("main:home_view")
        brand=Brand.objects.get(pk=brand_id)
        brand.delete()
        messages.success(request, 'The brand has been deleted successfully!','alert-success')
        return redirect("main:home_view")
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}",'alert-danger')
        return redirect('main:home_view')

def details_brand_view(request:HttpRequest, brand_id):
    try:
        brand=Brand.objects.get(pk=brand_id)
        cars=Car.objects.filter(brand=brand)
        return render(request,'brands/details_brand.html',{"brand":brand,"cars":cars}) 
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')
