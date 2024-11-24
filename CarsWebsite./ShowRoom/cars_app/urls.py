from django.urls import path
from . import views

app_name ="cars_app"

urlpatterns = [
    path('all/',views.all_cars_view, name='all_cars_view'),
    path('details/<int:car_id>/', views.car_detail_view, name='car_detail_view'),
    path('new/', views.new_car_view, name='new_car_view'),
    path('update/<int:car_id>/',views.update_car_view, name='update_car_view'),
    path('delete/<int:car_id>/',views.delete_car_view, name='delete_car_view'),
]