from django.urls import path
from .import views


app_name = "cars"

urlpatterns = [
    path("new/", views.add_new_car_view, name="add_new_car_view"),
    path("all/", views.all_cars_view, name="all_cars_view"),
    path("details/<int:car_id>", views.car_details_view, name="car_details_view"),
    path("update/", views.car_update_view, name="car_update_view"),
    path("delete/", views.car_delete_view, name="car_delete_view"),

]