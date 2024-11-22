from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path('add/', views.addBrandView, name="addBrandView"),
    path('update/<int:brandid>', views.updateBrandView, name="updateBrandView"),
    path('all/', views.displayBrandsView, name="displayBrandsView"),
]