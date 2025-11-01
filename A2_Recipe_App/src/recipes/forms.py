from django import forms


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
        label = "Cooking time (minutes)",
        required=False,
        )
    difficulty = forms.ChoiceField(
        choices=DIFFICULTY__CHOICES, 
        required=False
        )
    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES, 
        required=False 
        )
    
