from django.urls import path
from . import views

app_name = "publishers"

urlpatterns = [
    path("add/", views.add_publisher, name="add_publisher"),
    path("all/", views.publishers_page, name="publishers_page"),
    path("<publisher_id>/", views.publisher_page, name="publisher_page"),
]