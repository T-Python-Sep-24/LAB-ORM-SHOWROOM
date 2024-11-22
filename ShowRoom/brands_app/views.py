from django.shortcuts import render,redirect
from .models import Brand

def all_brands_view(request):
    brands = Brand.objects.all()  # Fetch all brands from the database
    return render(request, 'brands_app/all_brands.html', {'brands': brands})

def brand_detail_view(request):
    return render(request, 'brands_app/brand_detail.html')

def new_brand_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        logo = request.FILES['logo']
        about = request.POST['about']
        founded_at = request.POST['founded_at']
        
        # Create and save the new brand
        Brand.objects.create(name=name, logo=logo, about=about, founded_at=founded_at)
        
        # Redirect to the all brands view
        return redirect('brands_app:all_brands_view')  # Ensure this matches your URL pattern

    return render(request, 'brands_app/new_brand.html')

def update_brand_view(request):
    return render(request, 'brands_app/update_brand.html')  


