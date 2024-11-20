from django.urls import path
from . import views 

app_name = "main"
urlpatterns = [
    path('', views.add_car_view, name='add_car_view'),
]