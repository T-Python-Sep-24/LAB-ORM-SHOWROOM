from django.contrib import admin
from .models import Color

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')  # Show these fields in the admin list view
    search_fields = ('name',)  # Enable searching by color name