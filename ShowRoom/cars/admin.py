from django.contrib import admin
from .models import Car, Color, CarReview
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "model_year")

admin.site.register(Car, CarAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "hexadecimal")

admin.site.register(Color, ColorAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", 'car', 'rating')

admin.site.register(CarReview, ReviewAdmin)