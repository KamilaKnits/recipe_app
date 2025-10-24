from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse
# Create your models here.

class Recipe(models.Model):
    name= models.CharField(max_length=120,help_text="Enter recipe name ")
    recipe_description= models.TextField(max_length=300, blank=True, help_text=" Enter a short description of the recipe ")
    ingredients= models.TextField(max_length=255, help_text="Enter the ingredients (comma separated)")
    cooking_time= models.IntegerField(help_text="Enter the cooking time in minutes", validators=[
            MinValueValidator(1, message="Cooking time must be at least 1 minute"),
            MaxValueValidator(1440, message="Cooking time cannot exceed 24 hours (1440 minutes)")
        ])
    difficulty= models.CharField(max_length=20,blank=True, help_text="Difficulty level calculated automatically")
    recipe_image= models.ImageField(upload_to='recipes', default='no_picture.jpg', help_text="Upload Image here")
    

    def return_ingredients_list(self):
        return [i.strip() for i in self.ingredients.split(",") if i.strip()]
    
    def calculate_difficulty(self):

        ingredients_list = self.return_ingredients_list()
        num_ingredients = len(ingredients_list)

        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        if self.cooking_time < 10 and num_ingredients >= 4:
            return "Medium"
        if self.cooking_time >= 10 and num_ingredients < 4:
            return "Intermediate"
        if self.cooking_time >= 10 and num_ingredients >=4:
            return "Hard"

    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})    

    def __str__ (self):
        return  str(self.name)