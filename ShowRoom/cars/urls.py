from django.urls import path 
from . import views

app_name = "cars"

urlpatterns = [
    path('all',views.all_cars_view,name="all_cars_view"),
    path('add/',views.add_car_view,name="add_car_view"),
    path('update/<car_id>',views.update_view,name="update_view"),
    path('update/<car_id>',views.update_view,name="update_view"),
    path('detail/<car_id>',views.detail_view,name="detail_view"),
    path('delete/<car_id>',views.delete_view,name="delete_view"),
]