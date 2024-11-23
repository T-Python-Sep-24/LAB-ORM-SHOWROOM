from django.urls import path
from . import views



app_name='brands'

urlpatterns = [
    path('create/',views.new_brand_view,name="new_brand_view"),
    path('all/',views.all_brands_view,name="all_brands_view"),
    path('detail/<brand_id>',views.brand_detail_view,name="brand_detail_view"),
    path('update/<brand_id>',views.brand_update_view,name="brand_update_view"),
    path('delete/<brand_id>',views.delete_brand_view,name="delete_brand_view"),

]