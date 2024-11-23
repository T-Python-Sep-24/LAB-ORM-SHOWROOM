from django.contrib import admin
from .models import Brand
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display=['name','founded_at']
    list_filter=['founded_at',]
admin.site.register(Brand,BrandAdmin)