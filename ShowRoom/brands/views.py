from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpRequest,HttpResponse
from .models import Brand

# Create your views here.
def all_brands_view(request: HttpRequest):
    brands = Brand.objects.all()
    for brand in brands:
        brand.car_count = brand.cars.count()  
    return render(request, "brands/all_brands.html", {"brands": brands})



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


def brand_detail_view(request:HttpRequest,brand_id:int):
    brand = Brand.objects.get(pk=brand_id)
    return render(request,"brands/detail.html",{"brand":brand})

def brand_delete_view(request:HttpRequest,brand_id:int):
    brand = Brand.objects.get(pk=brand_id)
    brand.delete()
    return render(request,"brands/all_brands.html",{"brand":brand})

def brand_update_view(request:HttpRequest,brand_id:int):
    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == "POST":
        brand.name = request.POST["name"]
        brand.about = request.POST["about"]
        brand.founded_at = request.POST["founded_at"]
        if request.FILES.get("logo"):
            brand.logo = request.FILES["logo"]
        
        brand.save()
        return redirect("brands:all_brands_view") 
    return render(request, "brands/update.html", {"brand": brand})