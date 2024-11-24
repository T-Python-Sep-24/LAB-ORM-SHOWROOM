from django.contrib import admin

from brands.models import Brand  # Import the Brand model

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_at')  # Display brand name and founded year in the admin list view
    search_fields = ('name',)  # Add search functionality for brand name
    list_filter = ('founded_at',)  # Add filter for founding year
