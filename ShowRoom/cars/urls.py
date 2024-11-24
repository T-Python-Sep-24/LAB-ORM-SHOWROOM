from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path('cars/all/', views.all_cars_view, name='all_cars_view'),
    path('cars/new/', views.new_car_view, name='new_car_view'),
    path('cars/update/<car_id>/', views.update_car_view, name='update_car_view'),
    path('cars/details/<car_id>/', views.details_car_view, name='details_car_view'),
    path('cars/colors/new/', views.new_color_view, name='new_color_view'),
    path('cars/colors/update/<color_id>/', views.update_color_view, name='update_color_view'),
    
]
