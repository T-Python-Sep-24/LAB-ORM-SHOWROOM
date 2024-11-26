from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
   
      path('signup/', views.sign_up_view, name='sign_up_view'),
      path('signin/', views.sign_in_view, name='sign_in_view'),
      path('logout/', views.logout_view, name='logout_view'),
]