from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Brand
from .forms import BrandForm

# Create your views here.
def all_brands_view(request: HttpRequest):
    brands = Brand.objects.all()
    if "search" in request.GET:
        brands = brands.filter(name__contains=request.GET["search"])

    context = {"brands": brands}    
    return render(request, "brands/all.html", context)


def new_brand_view(request: HttpRequest):
    if request.method == "POST":
        brand_form = BrandForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            return redirect("brands:all_brands_view")
        else:
            print("form error: ", brand_form.errors)

    return render(request, "brands/new.html")


def update_brand_view(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(pk=brand_id)
    context = {"brand": brand}

    if request.method == "POST":
        # updating an existing object (car) not creating new one
        brand_form = BrandForm(instance=brand, data=request.POST, files=request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            return redirect("brands:all_brands_view")
        else:
            print("form error: ", brand_form.errors)

    return render(request, "brands/update.html", context)