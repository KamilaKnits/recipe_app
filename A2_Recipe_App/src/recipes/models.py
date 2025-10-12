from django.db import models

# Create your models here.

difficulty_levels = [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Intermediate', 'Intermediate'),
    ('Hard', 'Hard'),
]

class Recipe(models.Model):
    name= models.CharField(max_length=50)
    ingredients= models.TextField(max_length=255)
    cooking_time= models.IntegerField()
    difficulty= models.CharField(max_length=20, choices= difficulty_levels)



    def __str__ (self):
        return  str(self.name)