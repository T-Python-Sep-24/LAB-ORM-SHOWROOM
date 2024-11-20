from django.contrib import admin
from .models import Car, Color
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "model_year")
admin.site.register(Car, CarAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "hexadecimal")
admin.site.register(Color, ColorAdmin)