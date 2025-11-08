from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from .forms import RecipeSearchForm


# model tests

class RecipeModelTest(TestCase):
    
    def setUpTestData():
        
        Recipe.objects.create(
            name= 'Chicken Soup', 
            ingredients= 'Water, Chicken, Carrots, Potatoes, Salt',
            cooking_time= 10,
            difficulty= 'Hard',
        )
    
    def test_recipe_name(self):
        
        recipe= Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name 

        self.assertEqual(field_label, 'name')

    def test_recipe_ingredients(self):

        recipe= Recipe.objects.get(id=1)
        max_length= recipe._meta.get_field('ingredients').max_length

        self.assertEqual(max_length, 255)

    def test_recipe_cooking_time(self):

        recipe= Recipe.objects.get(id=1)
        
        self.assertIsInstance(recipe.cooking_time, int)
        self.assertEqual(recipe.cooking_time, 10)

    def test_recipe_difficulty(self):

        recipe= Recipe.objects.get(id=1)
        max_length= recipe._meta.get_field('difficulty').max_length

        self.assertEqual(max_length, 20)

# views tests

class RecipeViewTest(TestCase):
    def setup(self):
        self.recipe1 = Recipe.objects.create(
            name = 'Brownies', 
            ingredients = 'Butter, Sugar, Vanilla Extract, Eggs, Flour, Cocoa Powder',
            cooking_time = 45,
            difficulty = 'Hard',
        )
        self.recipe2 = Recipe.objects.create(
            name = 'Pancakes', 
            ingredients = 'Flour, Sugar, Eggs, Milk, Butter',
            cooking_time = 10,
            difficulty = 'Hard', 
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')
        self.assertContains(response, 'Brownies')
        self.assertContains(response, 'Pancakes')

    
    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:detail'))
        self.assertTemplateUsed(response, 'recipes/recipes_detail.html')
        self.assertContains(response, 'Brownies')
        

# form tests

class RecipeFormTest(TestCase):
    def test_form_field_labels(self):
        form = RecipeSearchForm()
        self.assertEqual(form.fields['recipe_name'].label, 'Recipe name')
        self.assertEqual(form.fields['ingredient'].label, 'Ingredients')
        self.assertEqual(form.fields['cooking_time'].label, 'Cooking Time (minutes)')
        self.assertEqual(form.fields['difficulty'].label, 'Difficulty')
        self.assertEqual(form.fields['chart_type'].label, 'Chart Type')
    
    def test_valid_form(self):
        form = RecipeSearchForm(data = {
            'recipe_name':'Chicken Soup',
            'ingredient': 'Water, Chicken, Carrots, Potatoes, Salt',
            'cooking_time': '10',
            'difficulty': 'Hard',    
        })

        self.assertTrue(form.is_valid())

    def test_invalid_cooking_time(self):
        form = RecipeSearchForm(data = {
            'cooking_time': 'ten'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('cooking_time', form.errors)
        

    def test_empty_form_is_valid(self):
        form = RecipeSearchForm(data = {})

        self.assertTrue(form.is_valid())





    
    


