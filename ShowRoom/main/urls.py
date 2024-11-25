from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
