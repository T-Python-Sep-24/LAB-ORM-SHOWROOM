from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('all/', views.all_cars_view, name='all_cars_view'),
    path('new/', views.add_car_view, name='add_car_view'),
    path('<car_id>/details/', views.car_details_view, name='car_details_view'),
    path('<car_id>/update/', views.update_car_view, name='update_car_view'),
    path('<car_id>/delete/', views.delete_car_view, name='delete_car_view'),

    path('colors/new/', views.new_color_view, name='new_color_view'),
    path('colors/update/<color_id>', views.update_color_view, name='update_color_view'),


]