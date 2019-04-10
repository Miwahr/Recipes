from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

app_name = 'RecipesApp'
urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Рецепты
    url(r'^recipes$', views.recipes, name='recipes'),
    # страница рецепта
    url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
    # новый рецепт
    url(r'^new_recipe/$', views.new_recipe, name='new_recipe'),
    # редактирование рецепта
    url(r'^edit_recipe/(?P<recipe_id>\d+)/$', views.edit_recipe, name='edit_recipe'),
    # поиск
    url(r'^search/$', views.search, name='search'),
    # рейтинг ингредиентов
    url(r'^rating/$', views.rating, name='rating'),
    # рейтинг рецепта
    url(r'^rating_recipe/(?P<recipe_id>\d+)/$', views.rating_recipe, name='rating_recipe'),
    # добавление комментария
    url(r'^add_comment/(?P<recipe_id>\d+)/$', views.add_comment, name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, }),
    ]
