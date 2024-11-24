from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/', views.log_out, name="log_out"),
]