from django.contrib import admin
from .models import Game, Review, Category

# Register your models here.

class GameAdmin(admin.ModelAdmin):

    list_display = ("title", "publisher", "rating")
    list_filter = ("rating",)


class ReviewAdmin(admin.ModelAdmin):

    list_display =  ("user", "game", "rating")
    list_filter = ("game", "rating")

admin.site.register(Game, GameAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)