from django.urls import path 
from . import views

app_name = "brands"

urlpatterns = [
    path('all',views.all_brands_view,name="all_brands_view"),
    path('add',views.add_brand_view,name="add_brand_view"),
    path('detail/<brand_id>',views.brand_detail_view,name="brand_detail_view"),
    path('delete/<brand_id>',views.brand_delete_view,name="brand_delete_view"),
    path('update/<brand_id>',views.brand_update_view,name="brand_update_view"),

]