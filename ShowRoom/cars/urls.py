from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path('add/', views.addCarView, name="addCarView"),
    path('<filter>/', views.displayCarsView, name="displayCarsView"),
    
    path('color/add/', views.addColorView, name="addColorView"),
    path('color/update/<int:clrId>', views.updateColorView, name="updateColorView"),

]