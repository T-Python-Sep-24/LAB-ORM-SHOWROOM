from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('all/', views.all_brands_view, name='all_brands_view'),
    path('add/', views.add_brand_view, name='add_brand_view'),
    path('<brand_id>/update/', views.update_brand_view, name='update_brand_view'),
    path('<brand_id>/delete/', views.delete_brand_view, name='delete_brand_view'),
    path('<brand_id>/details/', views.brand_details_view, name='brand_details_view')

]