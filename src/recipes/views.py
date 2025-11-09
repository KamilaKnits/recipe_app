from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Recipe
from .forms import RecipeSearchForm, RecipeAddForm
from .utils import get_chart
import pandas as pd

# Create your views here

def home(request):
    return render(request, 'recipes/recipes_home.html')

# class-based view
class RecipeListView(LoginRequiredMixin, ListView):
     # specify model
    model = Recipe
    # specify template
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'

@login_required
def recipes_search(request):

    form = RecipeSearchForm(request.POST or None)
    recipes = None
    chart = None
   
    

    if request.method == 'POST' and form.is_valid():
        # extract from data
        recipe_name = form.cleaned_data.get('recipe_name') # pulling forms.py RecipeSearchForm()
        ingredients = form.cleaned_data.get('ingredient')
        cooking_time = form.cleaned_data.get('cooking_time')
        difficulty = form.cleaned_data.get('difficulty')
        chart_type = form.cleaned_data.get('chart_type')
        
        qs = Recipe.objects.all() # get all recipes 
        if recipe_name:
            qs = qs.filter(name__icontains=recipe_name)
        if ingredients:
            qs = qs.filter(ingredients__icontains = ingredients)
        if cooking_time:
            qs = qs.filter(cooking_time__lte = cooking_time)
        if difficulty:
            qs = qs.filter(difficulty=difficulty)    
            
        # convert querysets values to pandas dataframe
        recipes = qs
            
        df = pd.DataFrame(qs.values('name', 'cooking_time', 'difficulty'))
        if not df.empty:
            chart_data = {
                'name': df['name'].tolist(),
                'cooking_time': df['cooking_time'].tolist(),
                'difficulty': df['difficulty'].tolist(),
            }
            chart = get_chart(chart_type, chart_data)

    context = {
        'form': form,
        'recipes': recipes,
        'chart': chart,
        
        
    }
    return render(request, 'recipes/recipes_search.html', context) # create file

@login_required
def add_recipe_view(request):

    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
    
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            messages.success(request, 'Recipe added successfully!')

            return redirect('recipes:detail', pk=recipe.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RecipeAddForm()
           
    return render(request, 'recipes/recipe_add.html', {'form': form})    