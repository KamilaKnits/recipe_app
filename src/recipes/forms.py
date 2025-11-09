from django import forms
from .models import Recipe

DIFFICULTY__CHOICES = (
    ('', 'All Difficulty levels'),
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Intermediate', 'Intermediate'),
    ('Hard', 'Hard')
)

CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Plot'),
)

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(
        label = "Recipe name",
        required=False,
        )
    ingredient = forms.CharField(
        label= "Ingredients",
        required=False,
        )
    cooking_time= forms.IntegerField(
        label = "Cooking Time (minutes)",
        required=False,
        )
    difficulty = forms.ChoiceField(
        label = "Difficulty",
        choices=DIFFICULTY__CHOICES, 
        required=False
        )
    chart_type = forms.ChoiceField(
        label = "Chart Type",
        choices=CHART_CHOICES, 
        required=False 
        )
    
class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'recipe_name', 
            'ingredients', 
            'cooking_time',
            'recipe_description',
            'recipe_image',
            ]

    recipe_name = forms.CharField(
        label = "Recipe name",
        required=False,
        )
    ingredients = forms.CharField(
        label= "Ingredients",
        required=False,
        )
    cooking_time= forms.IntegerField(
        label = "Cooking Time (minutes)",
        required=False,
        )
    recipe_description= forms.CharField(
        label="Description",
        )
    difficulty = forms.ChoiceField(
        label = "Difficulty",
        choices=DIFFICULTY__CHOICES, 
        required=False
        )
    recipe_image= forms.ImageField(
        label='Recipe Image', 
        required=False
        )

    
