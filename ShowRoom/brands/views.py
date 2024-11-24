from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand , Review
from .forms import BrandForm , ReviewForm  
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

def is_admin(user):
    return user.is_superuser


def all_brands(request):
    brands = Brand.objects.all()
    
    
    brand_filter = request.GET.get('brand', None)
    search = request.GET.get('search', '')

    
    if brand_filter:
        brands = brands.filter(id=brand_filter)
    if search:
        brands = brands.filter(name__icontains=search)

   
    paginator = Paginator(brands, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'brands/all_brands.html', {
        'page_obj': page_obj,
        'brand_filter': brand_filter,
        'search': search,
    })

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    reviews = brand.brand_reviews.all()
    
    review_form = ReviewForm(request.POST or None)
    
    if request.method == "POST" and review_form.is_valid():
        review = review_form.save(commit=False)
        review.brand = brand
        review.user = request.user
        review.save()
        
        reviews = brand.brand_reviews.all()
    
    star_range = range(1, 6)

    return render(request, 'brands/brand_details.html', {
        'brand': brand,
        'reviews': reviews,
        'review_form': review_form,
        'star_range': star_range,  
    })

@user_passes_test(is_admin)
def new_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, 'The brand has been added successfully!')
            return redirect('brands:all_brands')  
    else:
        form = BrandForm()

    return render(request, 'brands/new_brand.html', {'form': form})

@user_passes_test(is_admin)
def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, f"Brand '{brand.name}' has been successfully updated!")
            return redirect('brands:brand_detail', brand_id=brand.id)  
    else:
        form = BrandForm(instance=brand)  

    return render(request, 'brands/update_brand.html', {'form': form, 'brand': brand})

@user_passes_test(is_admin)
def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, f"Brand '{brand.name}' has been successfully deleted!")
        return redirect('brands:all_brands')  
    
    return render(request, 'brands/delete_brand.html', {'brand': brand})

@user_passes_test(is_admin)
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if not request.user.is_superuser:
        raise Http404("You do not have permission to delete this review.")
    
    review.delete()
    
    messages.success(request, "Review deleted successfully!")

    return redirect('brands:brand_detail', brand_id=review.brand.id)
