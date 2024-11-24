from . import views
from django.urls import path

app_name="cars"

urlpatterns=[
    path('all/',views.all_cars_view, name="all_cars_view"),
    path('details/<car_id>/',views.detail_car_view, name="detail_car_view"),
    path('new/',views.new_car_view, name="new_car_view"),
    path('update/<car_id>/',views.update_car_view, name="update_car_view"),
    path('delete/<car_id>/',views.delete_car_view, name="delete_car_view"),
    path('colors/update/<color_id>/',views.update_color_view, name="update_color_view"),
    path('colors/new/',views.new_color_view, name="new_color_view"),
    path('colors/delete/<color_id>/',views.delete_color_view,name="delete_color_view"),
    path('colors/search_color/', views.search_color, name='search_color'),
]