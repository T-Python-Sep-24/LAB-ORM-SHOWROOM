from django.urls import path
from . import views

app_name="cars_app"

urlpatterns = [
    path('all/', views.all_cars_view, name='all_cars_view'),  
    path('details/<card_id>/', views.car_detail_view, name='car_detail_view'),  
    path('new/', views.new_car_view, name='new_car_view'), 
    path('update/<car_id>/', views.update_car_view, name='update_car_view'), 
    path('colors/new/', views.new_color_view, name='new_color_view'), 
    path('colors/all/', views.all_colors_view, name='all_colors_view'), 
    path('colors/update/<color_id>/', views.update_color_view, name='update_color_view'), 


]