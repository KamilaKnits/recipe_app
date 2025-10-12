from django.test import TestCase
from .models import Recipe

# Create your tests here.

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

    
    


