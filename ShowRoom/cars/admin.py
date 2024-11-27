from django.contrib import admin
from .models import Car, Color,Review

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'price')
    search_fields = ('name', 'brand__name')
    list_filter = ('brand', 'model', 'colors')
filter_horizontal = ('colors',) 

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code', 'photo')  # Display the name, hex_code, and photo in the admin list view
    search_fields = ('name', 'hex_code')  # Allow searching by color name and hex_code
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'rating', 'created_at')  
    list_filter = ('rating', 'created_at')  
    search_fields = ('user__username', 'car__name', 'review_text')  
    ordering = ('-created_at',)  