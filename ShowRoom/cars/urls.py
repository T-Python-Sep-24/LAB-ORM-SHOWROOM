from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("all/", views.all_cars_view, name="all_cars_view"),
    path("new/", views.new_car_view, name="new_car_view"),
    path("update/<car_id>/", views.update_car_view, name="update_car_view"),
]