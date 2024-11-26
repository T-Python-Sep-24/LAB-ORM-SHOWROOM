from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path('add/', views.addCarView, name="addCarView"),
    path('update/<int:carId>', views.updateCarView, name="updateCarView"),
    path('delete/<int:carId>', views.deleteCarView, name="deleteCarView"),
    path('cardetails/<int:carId>', views.carDetailsView, name="carDetailsView"),
    path('<filter>/', views.displayCarsView, name="displayCarsView"),
    
    path('color/add/', views.addColorView, name="addColorView"),
    path('color/update/<int:clrId>', views.updateColorView, name="updateColorView"),
    path('color/delete/<int:clrId>', views.deleteColorView, name="deleteColorView"),
    path('colors/all/', views.allColorsView, name="allColorsView"),

    path('comment/add/<int:carId>', views.addCommentView, name="addCommentView"),
    path('comment/delete/<int:commentId>', views.deleteCommentView, name="deleteCommentView"),

    path('bookmark/<int:carId>', views.addBookmarkView, name="addBookmarkView"),
]