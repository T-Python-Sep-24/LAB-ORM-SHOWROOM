from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('all/', views.all_cars, name='all_cars'),
    path('details/<int:car_id>/', views.car_details, name='car_details'),
    path('add/', views.add_car, name='add_car'),
    path('update/<int:car_id>/', views.update_car, name='update_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
    path('color/add', views.add_color, name='add_color'),
    path('color/update/<int:color_id>/', views.update_color, name='update_color'),
    path('color/<int:color_id>/', views.delete_color, name='delete_color'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)