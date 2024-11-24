from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Brand
from .forms import BrandForm

# Create your views here.
def all_brands_view(request: HttpRequest):
    brands = Brand.objects.all()
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