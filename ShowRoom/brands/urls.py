from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('all/', views.all_brands, name='all_brands'),  # List all brands
    path('details/<int:brand_id>/', views.brand_detail, name='brand_detail'),  # Brand detail page
    path('new/', views.new_brand, name='new_brand'),  # Add new brand
    path('update/<int:brand_id>/', views.update_brand, name='update_brand'),  # Update brand
    path('delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),  # Delete brand
]
