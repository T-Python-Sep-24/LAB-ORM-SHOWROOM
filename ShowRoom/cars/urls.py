from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "cars"

urlpatterns = [
    path('all/', views.all_cars, name='all_cars'),
    path('new/', views.create_car, name='create_car'),
    path('details/<int:car_id>/', views.car_detail, name='car_detail'),
    path('update/<int:car_id>/', views.update_car, name='update_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
    path("reviews/add/<int:car_id>/", views.add_review_view, name="add_review_view"),
    path("bookmarks/add/<int:car_id>/", views.add_bookmark_view, name="add_bookmark_view")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
