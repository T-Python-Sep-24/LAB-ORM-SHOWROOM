from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path('add/', views.addCarView, name="addCarView"),
    path('update/<int:carid>', views.updateCarView, name="updateCarView"),
    path('cardetails/<int:carid>', views.carDetailsView, name="carDetailsView"),
    path('<filter>/', views.displayCarsView, name="displayCarsView"),
    
    path('color/add/', views.addColorView, name="addColorView"),
    path('color/update/<int:clrId>', views.updateColorView, name="updateColorView"),

]