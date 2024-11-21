from django.urls import path
from . import views


app_name = "brands"

urlpatterns = [
    path("brands/all/", views.all_brands, name="all_brands"),
    path("brands/new/", views.create_brand, name="create_brand"),
    path("brands/details/<brand_id>/", views.brand_detail, name="brand_detail"),
    path("brands/update/<brand_id>/", views.brand_update, name="brand_update"),
    path("brands/delete/<brand_id>/", views.brand_delete, name="brand_delete"),
]