from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path('add/', views.addBrandView, name="addBrandView"),
    path('update/<int:brandId>', views.updateBrandView, name="updateBrandView"),
    path('delete/<int:brandId>', views.deleteBrandView, name="deleteBrandView"),
    path('branddetails/<int:brandId>', views.brandDetailsView, name="brandDetailsView"),
    path('all/', views.displayBrandsView, name="displayBrandsView"),
]