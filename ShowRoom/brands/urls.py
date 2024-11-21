from django.urls import path
from . import views

urlpatterns = [
    path('', views.brands_home, name='brands_home'),  # Brands main page
    path('', views.brand_list, name='brand_list'),  # List all brands
    path('<int:brand_id>/', views.brand_detail, name='brand_detail'),  # Brand details
]


