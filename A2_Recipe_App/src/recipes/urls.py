from django.urls import path
from .views import RecipeListView, RecipeDetailView, home, recipes_search

app_name= 'recipes'

urlpatterns= [
    path('', home, name = 'home'),
    path('list/', RecipeListView.as_view(), name = 'list'),
    path('list/<pk>', RecipeDetailView.as_view(), name = 'detail'),
    path('search', recipes_search, name = 'search'),
]