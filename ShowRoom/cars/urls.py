from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('all/', views.all_cars, name='all_cars'),  # List all cars
    path('details/<int:car_id>/', views.car_detail, name='car_detail'),  # Car detail page
    path('new/', views.new_car, name='new_car'),  # Add new car
    path('update/<int:car_id>/', views.update_car, name='update_car'),  # Update car
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),  # Delete car
    path('colors/new/', views.new_color, name='new_color'),  # Add new color
    path('colors/update/<int:color_id>/', views.update_color, name='update_color'),  # Update color
]
