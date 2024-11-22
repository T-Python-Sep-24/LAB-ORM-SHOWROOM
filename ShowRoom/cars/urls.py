from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path('cars/all/', views.all_cars, name='all_cars'),
    path('cars/new/', views.create_car, name='create_car'),
    path('cars/details/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/update/<int:car_id>/', views.update_car, name='update_car'),
    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),
]
