from django.urls import path
from .import views


app_name = "cars"

urlpatterns = [
    path("all-cars/", views.all_cars_view, name="all_cars_view"),
]