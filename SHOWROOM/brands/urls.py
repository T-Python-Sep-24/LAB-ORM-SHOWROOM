from django.urls import path
from .import views


app_name = "brands"

urlpatterns = [
    path("new/", views.add_new_brand_view, name="add_new_brand_view"),
    path("all/", views.all_brands_view, name="all_brands_view"),
    path("details/<int:brand_id>", views.brand_details_view, name="brand_details_view"),
    path("update/<int:brand_id>", views.brand_update_view, name="brand_update_view"),
    path("delete/<int:brand_id>", views.brand_delete_view, name="brand_delete_view"),

]