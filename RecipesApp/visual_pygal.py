import pygal
from RecipesProject.settings import MEDIA_ROOT

def visual_ingred(d: dict):
    """Визуализация ингредиентов"""
    hist = pygal.Bar()

    hist.title = "Частота появления ингредиентов"
    hist.x_labels = [i for i in d.keys()]
    hist.x_title = "Ингредиенты"
    hist.y_title = "Количество"
    hist.add("ингредиенты", [i for j, i in d.items()])
    hist.render_to_file(MEDIA_ROOT + '/ingred.svg')

