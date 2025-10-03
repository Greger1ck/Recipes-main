from django.shortcuts import render
from django.views.generic import (
    ListView,

)
from recipes.models import Category, Recipe



class IndexPage(ListView):
    template_name = 'recipes/index.html'
    model = Recipe
    context_object_name = "recipes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context

