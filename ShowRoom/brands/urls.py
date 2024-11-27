from . import views
from django.urls import path


app_name = "brands"

urlpatterns=[

    path("brands/",views.all_brands_view,name="all_brand_view"),
    path("add/brand/",views.add_brand_view,name="add_brand_view"),
    path("detail/brand/<brand_id>/",views.brand_detail_view,name="detail_brand_view"),
    path("update/<brand_id>/",views.update_brand_view,name="update_brand_view"),
    path("delete/<brand_id>/",views.delete_brand_view,name="delete_brand_view"),
   
]