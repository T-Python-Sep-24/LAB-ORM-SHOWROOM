from django.shortcuts import render

# Create your views here.
def all_cars_view(request):
   
    return render(request, 'cars_app/all_cars.html')

def car_detail_view(request):
   
    return render(request, 'cars_app/car_detail.html', )

def new_car_view(request):
       
    return render(request, 'cars_app/new_car.html')

def update_car_view(request):
      
    return render(request, 'cars_app/update_car.html')

def new_color_view(request):
      
    return render(request, 'cars_app/new_color.html')

def update_color_view(request):

    return render(request, 'cars_app/update_color.html')



