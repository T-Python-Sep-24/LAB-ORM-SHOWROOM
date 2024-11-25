from django.urls import path
from . import views


app_name = "brands"

urlpatterns = [
    path("all/", views.all_brands_view, name="all_brands_view"),
    path("details/<brand_id>/", views.brand_detail_view, name="brand_detail_view"),
    path("new/", views.new_brand_view, name="new_brand_view"),
    path("search/brands/", views.search_brands_view, name="search_brands_view"),
]

