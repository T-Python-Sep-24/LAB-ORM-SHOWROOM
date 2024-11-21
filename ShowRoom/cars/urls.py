from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_home, name='cars_home'),  # Cars main page
    path('', views.car_list, name='car_list'),  # List all cars
    path('<int:car_id>/', views.car_detail, name='car_detail'),
]
