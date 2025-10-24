from django.urls import path
from .views import RecipeListView, RecipeDetailView, home

app_name= 'recipes'

urlpatterns= [
    path('', home, name = 'home'),
    path('list/', RecipeListView.as_view(), name = 'list'),
    path('list/<pk>', RecipeDetailView.as_view(), name = 'detail'),
]