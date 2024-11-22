from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import BrandForm
from .models import Brand
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def all_brands_view(request:HttpRequest):
    return render(request,'brands/all_brands.html')

def new_brand_view(request:HttpRequest):
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

def delete_brand_view(request:HttpRequest):
    return render(request,'brands/all_brands.html')

def details_brand_view(request:HttpRequest, brand_id):
    try:
        brand=Brand.objects.get(pk=brand_id)

        return render(request,'brands/details_brand.html',{"brand":brand}) 
    except Brand.DoesNotExist:
        print("error massege")
        messages.error(request, "An error occurred: The page not found",'alert-danger')
        return redirect('main:home_view')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('main:home_view')
