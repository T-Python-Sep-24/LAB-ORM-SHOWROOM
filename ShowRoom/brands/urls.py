from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path("all/", views.all_brands_view, name="all_brands_view"),
    path("new/", views.new_brand_view, name="new_brand_view"),
    path("update/<brand_id>/", views.update_brand_view, name="update_brand_view"),
    path("details/<brand_id>/", views.details_brand_view, name="details_brand_view"),
    path("delete/<brand_id>/", views.delete_brand_view, name="delete_brand_view"),
]