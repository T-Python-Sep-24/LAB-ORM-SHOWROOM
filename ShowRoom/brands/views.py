from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Brand

# Create your views here.
def all_brands_view(request:HttpRequest):
    brands = Brand.objects.all()
    return render(request,"brands/all_brands.html",{"brands":brands})

def add_brand_view(request:HttpRequest):
        

    if request.method == "POST":
        new_brand = Brand(
            name=request.POST["name"],
            about=request.POST["about"],
            logo=request.FILES["logo"],
            website=request.POST["website"],
            founded_at=request.POST["founded_at"],
                        )
        
        new_brand.save()
        
        return redirect("brands:all_brand_view")
    return render(request,"brands/add_brand.html")