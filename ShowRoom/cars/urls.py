from django.urls import path
from . import views 

app_name = "cars"
urlpatterns = [
    path('new/', views.manage_car_view, name="add_car"),
    path('update/<car_id>/',views.manage_car_view, name="update_car"),
    path('colors/new/', views.manage_color_view, name="add_color"),
    path('colors/update/<color_id>/', views.manage_color_view, name ="update_color"),
    path('all/',views.all_cars_view, name="all_cars_view"),
    path('details/<card_id>/',views.car_details_view,name="car_details_view"),
    path('delete/<car_id>/', views.delete_car, name='delete_car'),
    path('colors/delete/<color_id>/', views.delete_color, name='delete_color'),
    path('<car_id>/review/', views.manage_car_view, name='add_review'),
]