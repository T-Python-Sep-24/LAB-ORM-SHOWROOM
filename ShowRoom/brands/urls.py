from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path("all/", views.all_brands_view, name="all_brands_view"),
    path("new/", views.new_brand_view, name="new_brand_view"),
]