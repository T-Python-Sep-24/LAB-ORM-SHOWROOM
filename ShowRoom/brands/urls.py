from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path("brands/new/", views.new_brand_view ,  name="new_brand_view"),
    path("brands/all/" , views.all_brands_view,  name="all_brands_view"), 
    path("brands/details/<brand_id>/" , views.brand_detail_view , name="brand_detail_view"),
    path("brands/update/<brand_id>/" , views.update_brand_view , name="update_brand_view"), 
    
]