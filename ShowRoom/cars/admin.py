from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand']

admin.site.register(Car, CarAdmin)