from django.shortcuts import render
from django.views.generic import (
    ListView,

)
from recipes.models import Recipe




class IndexPage(ListView):
    template_name = 'recipes/index.html'
    model = Recipe
