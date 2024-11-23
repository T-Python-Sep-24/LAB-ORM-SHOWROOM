from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.all_brands, name='all_brands'),
    path('details/<int:brand_id>/', views.brand_details, name='brand_details'),
    path('add/', views.add_brand, name='add_brand'),
    path('update/<int:brand_id>/', views.update_brand, name='update_brand'),
    path('delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
]