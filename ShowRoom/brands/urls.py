from django.urls import path 
from . import views

app_name = "brands"

urlpatterns = [
    path('all',views.all_brands_view,name="all_brands_view"),
    path('add',views.add_brand_view,name="add_brand_view"),
]