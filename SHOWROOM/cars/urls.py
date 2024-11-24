from django.urls import path
from .import views


app_name = "cars"

urlpatterns = [
    path("new/", views.add_new_car_view, name="add_new_car_view"),
    path("all/", views.all_cars_view, name="all_cars_view"),
    path("details/<int:car_id>", views.car_details_view, name="car_details_view"),
    path("update/<int:car_id>", views.car_update_view, name="car_update_view"),
    path("delete<int:car_id>/", views.car_delete_view, name="car_delete_view"),
    path('colors/new/', views.add_new_color_view, name='add_new_color_view'),
    path('colors/update/<int:color_id>/', views.update_color_view, name='update_color_view'),
    path('car/<int:car_id>/add_review/', views.add_review_view, name='add_review_view'),

]