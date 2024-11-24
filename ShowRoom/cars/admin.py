from django.contrib import admin

# Register your models here. 
from . models import Car , Color 
from brands .models import Brand

admin.site.register(Car )
admin.site.register(Color)
admin.site.register(Brand)