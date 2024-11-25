from django.urls import path
from . import views


app_name = "cars"

urlpatterns = [
    path("<filter>/", views.all_cars_view, name="all_cars_view"),
    path("details/<car_id>/", views.car_detail_view, name="car_detail_view"),
    path("new/car/", views.new_car_view, name="new_car_view"),
    path("update/<car_id>/", views.car_update_view, name="car_update_view"),
    path("delete/<car_id>/", views.car_delete_view, name="car_delete_view"),
    path("colors/new/", views.new_color_view, name="new_color_view"),
    path("search/cars/", views.search_cars_view, name="search_cars_view"),
    path("reviews/add/<car_id>/", views.add_review_view, name="add_review_view")
]
