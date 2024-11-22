from django.contrib import admin
from .models import Car, Color

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'price')
    search_fields = ('name', 'brand__name')
    list_filter = ('brand', 'model', 'colors')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')
    search_fields = ('name', 'hex_code')
