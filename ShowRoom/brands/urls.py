from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path('add/', views.addBrandView, name="addBrandView"),
    path('update/<int:brandid>', views.updateBrandView, name="updateBrandView"),
    path('delete/<int:brandid>', views.deleteBrandView, name="deleteBrandView"),
    path('all/', views.displayBrandsView, name="displayBrandsView"),
    path('branddetails/<int:brandid>', views.brandDetailsView, name="brandDetailsView"),
]