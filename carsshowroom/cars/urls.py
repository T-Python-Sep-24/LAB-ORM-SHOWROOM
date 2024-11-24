from django.urls import path
from . import views



app_name='cars'

urlpatterns = [
    path('create/',views.new_car_view,name="new_car_view"),
    path('all/',views.all_cars_view,name="all_cars_view"),
    path('detail/<car_id>',views.car_detail_view,name="car_detail_view"),
    path('update/<car_id>',views.car_update_view,name="car_update_view"),
    path('delete/<car_id>',views.delete_car_view,name="delete_car_view"),
    path('colors/all/',views.all_colors_view,name='all_colors_view'),
    path('colors/new/',views.new_color_view,name='new_color_view'),
    path('colors/update/<color_id>/',views.color_update_view,name='color_update_view'),
    path('colors/delete/<color_id>',views.delete_color_view,name='delete_color_view'),
    path('add_review/<car_id>/',views.add_review_view,name="add_review_view")

    
]