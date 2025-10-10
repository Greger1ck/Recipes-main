from os import name
from django.shortcuts import render
from django.template import context
from django.views.generic import DetailView, ListView

from recipes.models import Category, Recipe

class IndexPage(ListView):
    template_name = 'recipes/index.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    

class RecipeDetailPage(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "recipes/recipe_detail.html"


class SearchPage(ListView):
    template_name = "recipes/search.html"
    context_object_name = "recipes"
    model = Recipe

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', None)
        if search :
            queryset = queryset.filter(name__icontains=search)
        return queryset
    
class CategoryList(DetailView):
    template_name = 'recipes/search.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
            obj = self.get_object()
            context = super().get_context_data(**kwargs)
            context["recipes"] = obj.recipes_by_cat.all()
            return context
        