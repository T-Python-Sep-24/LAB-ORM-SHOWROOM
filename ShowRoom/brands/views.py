from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Brand
from cars.models import Car
from .forms import BrandForm
from django.contrib import messages

# Create your views here.
def all_brands_view(request: HttpRequest):
    brands = Brand.objects.all()
    if "search" in request.GET:
        brands = brands.filter(name__contains=request.GET["search"])

    context = {"brands": brands}    
    return render(request, "brands/all.html", context)


def new_brand_view(request: HttpRequest):
    # Limit acces to admin
    if not request.user.is_superuser:
        messages.error(request, "This operation requires admin account","alert-danger")
        return redirect("accounts:sign_in")

    if request.method == "POST":
        brand_form = BrandForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            return redirect("brands:all_brands_view")
        else:
            print("form error: ", brand_form.errors)

    return render(request, "brands/new.html")


def update_brand_view(request: HttpRequest, brand_id: int):
    # Limit acces to admin
    if not request.user.is_superuser:
        messages.error(request, "This operation requires admin account","alert-danger")
        return redirect("accounts:sign_in")

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


def details_brand_view(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(pk=brand_id)
    cars = Car.objects.all().filter(brand=brand)
    context = {"brand": brand, "cars": cars}

    return render(request, "brands/details.html", context)


def delete_brand_view(request: HttpRequest, brand_id: int):
    # Limit acces to admin
    if not request.user.is_superuser:
        messages.error(request, "This operation requires admin account","alert-danger")
        return redirect("accounts:sign_in")

    brand = Brand.objects.get(pk=brand_id)
    brand.delete()

    return redirect("brands:all_brands_view")