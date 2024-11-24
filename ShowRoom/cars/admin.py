from django.contrib import admin
from .models import Car, Comment, Attachment, Color

class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'car']

admin.site.register(Car, CarAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Color)
admin.site.register(Attachment)