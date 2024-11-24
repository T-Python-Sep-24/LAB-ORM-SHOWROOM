from . import views
from django.urls import path


app_name="cars"


urlpatterns=[
    path("add/",views.add_car_view,name="add_car"),
    path('all/', views.all_cars_view, name='all_cars_view'),
    path("detail/<car_id>/",views.car_detail_view,name="car_detail_view"),
    path("update/<car_id>/",views.update_car_view,name="update_car_view"),
    path("delete/<car_id>/",views.delete_car_view,name="delete_car_view"),
    
    
    
]