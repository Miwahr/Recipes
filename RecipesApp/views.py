from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Recipe, Comment
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

from .visual_pygal import visual_ingred

def rating_ingred():
    d = {}
    for recipe in Recipe.objects.all():
        try:
            l = recipe.ingred.lower().split(',')
        except:
            l = []
        for i in l:
            i = i.strip()
            d[i] = d.setdefault(i, 0) + 1
    visual_ingred(d)

def check_recipe_owner(owner, user):
    """Проверка принадлежности рецепта пользователю"""
    if owner != user:
        raise Http404


def index(request):
    """Домашняя страница Сайта"""
    return render(request, 'RecipesApp/index.html')


def recipes(request):
    """Страница с рецептами"""
    recipes = Recipe.objects.order_by('date_added')
    context = {'recipes': recipes}
    return render(request, 'RecipesApp/recipes.html', context)


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.count_views += 1
    recipe.save()
    comments = recipe.comment_set.order_by('date_added')  # загрузка комментариев
    #print(comments.text)
    context = {'recipe': recipe, 'comments': comments}
    return render(request, 'RecipesApp/recipe.html', context)


@login_required
def new_recipe(request):
    """Определяет новый рецепт."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = RecipeForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = RecipeForm(request.POST, request.FILES)  # request.FILES - передаем еще и файлы
        if form.is_valid():
            form.save()
            rating_ingred()
            return HttpResponseRedirect(reverse('RecipesApp:recipes'))
    context = {'form': form}
    return render(request, 'RecipesApp/new_recipe.html', context)

@login_required
def edit_recipe(request, recipe_id):
    """Редактирование рецепта"""
    recipe = Recipe.objects.get(id=recipe_id)
    check_recipe_owner(recipe.owner, request.user)  # проверка владельца темы
    if request.method != 'POST':
        # исходный запрос, форма заполняется текущей записью
        form = RecipeForm(instance=recipe)
    else:
        # отправка данных POST, обработать данные
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            rating_ingred()
            return HttpResponseRedirect(reverse('RecipesApp:recipe', args=[recipe.id]))
    context = {'recipe': recipe, 'form': form}
    return render(request, 'RecipesApp/edit_recipe.html', context)


def search(request):
    """Страница поиска"""
    s_word = request.POST['s_word'].lower()
    d = {}
    for recipe in Recipe.objects.all():
        if s_word in recipe.ingred.lower() or s_word in recipe.name.lower() or s_word in recipe.text.lower():
            d[recipe.name] = recipe.id
    context = {'s_word': s_word, 'd': d}
    return render(request, 'RecipesApp/search.html', context)

def rating(request):
    """Страница рейтинга ингредиентов"""
    return render(request, 'RecipesApp/rating.html')


@login_required
def rating_recipe(request, recipe_id):
    """ Расчет рейтинга рецепта"""
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.rating_count += 1
    recipe.rating = round((recipe.rating * (recipe.rating_count-1) + int(request.POST['rating'])) / recipe.rating_count, 2)
    recipe.save()
    return HttpResponseRedirect(reverse('RecipesApp:recipe', args=[recipe.id]))


@login_required
def add_comment(request, recipe_id):
    """Добавление комментария"""
    comment = Comment()
    comment.text = request.POST['text']
    comment.owner = request.user
    recipe = Recipe.objects.get(id=recipe_id)
    comment.recipe = recipe
    comment.save()
    return HttpResponseRedirect(reverse('RecipesApp:recipe', args=[recipe_id]))
