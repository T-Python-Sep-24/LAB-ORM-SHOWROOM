from django.contrib import admin
from .models import Color,Car
# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)  

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')

admin.site.register(Color, ColorAdmin)
admin.site.register(Car, CarAdmin)


