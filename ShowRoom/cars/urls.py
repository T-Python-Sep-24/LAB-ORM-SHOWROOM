from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [  
    path('cars/all/', views.all_cars, name='all_cars'),
    path('cars/details/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/new/', views.new_car, name='new_car'),
    path('cars/update/<int:car_id>/', views.update_car, name='update_car'),
    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),

    path('cars/colors/new/', views.new_color, name='new_color'),
    path('cars/colors/update/<int:color_id>/', views.update_color, name='update_color'),
    path('cars/colors/delete/<int:color_id>/', views.delete_color, name='delete_color'),
]

