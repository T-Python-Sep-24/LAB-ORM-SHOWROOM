from django.shortcuts import render,redirect
from .models import Brand, Color  # Import your models

# Create your views here.
def all_cars_view(request):
   
    return render(request, 'cars_app/all_cars.html')

def car_detail_view(request):
   
    return render(request, 'cars_app/car_detail.html', )

def new_car_view(request):
    brands = Brand.objects.all()  # Fetch all brands
    colors = Color.objects.all()   # Fetch all colors

    return render(request, 'cars_app/new_car.html', {
        'brands': brands,
        'colors': colors
    })

def update_car_view(request):
      
    return render(request, 'cars_app/update_car.html')

def new_color_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hex_code = request.POST.get('hex_code')
        
        # Create a new Color instance
        Color.objects.create(name=name, hex_code=hex_code)
        
        # Redirect to the all colors view
        return redirect('cars_app:all_colors_view')  # Adjust the URL name as necessary

    return render(request, 'cars_app/new_color.html')
      
def update_color_view(request):

    return render(request, 'cars_app/update_color.html')


def all_colors_view(request):
    colors = Color.objects.all()  # Fetch all colors from the database
    return render(request, 'cars_app/all_colors.html', {'colors': colors})


