from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingred', 'text', 'image', 'owner']
        labels = {'name':'Название: ', 'ingred':'Ингредиенты: ', 'text':'Приготовление: ', 'image':'', 'owner':''}

