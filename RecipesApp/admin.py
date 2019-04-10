from django.contrib import admin
from RecipesApp.models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']



admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)