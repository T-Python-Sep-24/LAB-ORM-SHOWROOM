from django.urls import path
from . import views


app_name = "cars"

urlpatterns = [
    path("all/", views.all_cars_view, name="all_cars_view"),
    path("details/<car_id>/", views.car_detail_view, name="car_detail_view"),
    path("new/", views.new_car_view, name="new_car_view"),
    path("update/<car_id>/", views.car_update_view, name="car_update_view"),
    path("delete/<car_id>/", views.car_delete_view, name="car_delete_view"),
    path("colors/new/", views.new_color_view, name="new_color_view"),
    path("colors/update/<color_id>/", views.color_update_view, name="color_update_view"),
    path("delete/<color_id>/", views.color_delete_view, name="color_delete_view"),
    path("search/", views.search_cars_view, name="search_cars_view"),
]
