from django.contrib import admin
from .models import Color
from .models import Car

# Register your models here.

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
from django.contrib import admin

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'price', 'year')
    list_filter = ('brand', 'year')
    search_fields = ('model',)
