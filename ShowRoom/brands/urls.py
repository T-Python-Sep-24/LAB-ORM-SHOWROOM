from django.urls import path
from . import views 

app_name = "brands"
urlpatterns = [
    path('new/',views.manage_brand_view,name="add_brand"),
    path('update/<brand_id>/',views.manage_brand_view,name="update_brand"),
    path('all/', views.all_brands_view, name="all_brands_view"),
]