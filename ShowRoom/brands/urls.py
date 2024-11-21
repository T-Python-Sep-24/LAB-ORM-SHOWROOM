from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path('brands/all/', views.all_brands, name='all_brands'),
    path('brands/details/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('brands/new/', views.new_brand, name='new_brand'),
    path('brands/update/<int:brand_id>/', views.update_brand, name='update_brand'),
    path('brands/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
  
]