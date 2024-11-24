from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [  
    path('all/', views.all_cars, name='all_cars'),
    path('details/<int:car_id>/', views.car_detail, name='car_detail'),
    path('new/', views.new_car, name='new_car'),
    path('update/<int:car_id>/', views.update_car, name='update_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),

    path('colors/all/',views.all_colors ,name='all_colors'),
    path('colors/new/', views.new_color, name='new_color'),
    path('colors/update/<int:color_id>/', views.update_color, name='update_color'),
    path('colors/delete/<int:color_id>/', views.delete_color, name='delete_color'),
]

