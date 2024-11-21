from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.index_view, name="index_view"),
    path("cars/all/", views.all_cars, name="all_cars"),
    
]