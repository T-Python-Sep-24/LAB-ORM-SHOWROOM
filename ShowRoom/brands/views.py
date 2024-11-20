from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import BrandForm
from .models import Brand
# Create your views here.

def all_brands_view(request: HttpRequest):
    try:

        brands = Brand.objects.all()
        return render(request, 'all_brands.html', context={'brands': brands})

    except Exception as e:
        print(e)


def brand_details_view(request: HttpRequest, brand_id:int):
    brand = Brand.objects.get(pk=brand_id)
    return render(request, 'brand_details.html', context={'brand':brand})


def add_brand_view(request: HttpRequest):

    try:
        if request.method == "POST":
            brand_form = BrandForm(request.POST, request.FILES)
            if brand_form.is_valid():
                brand_form.save()
                messages.success(request, "Brand was Added successfully", "alert-success")
            else:
                print("brand form is not valid")
                messages.error(request, "Error in adding this brand", "alert-danger")

    except Exception as e:
        print(e)

def update_brand_view(request:HttpRequest, brand_id: int):
    brand = Brand.objects.get(pk=brand_id)

    if request.method == "POST":
        brand_form = BrandForm(request.POST, request.FILES, instance=brand)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, "Brand was updated successfully", "alert-success")
            return redirect("brands:brand_details_view", brand_id=brand_id)
        else:
            print("Brand update Form is not valid")

def delete_brand_view(request:HttpRequest, brand_id):
    try:
        brand = Brand.objects.get(pk=brand_id)
        brand.delete()
        messages.success(request, "Brand was deleted Successfully", "alert-success")
        return redirect(request, 'all_brands_view')
    except Exception as e:
        print(e)