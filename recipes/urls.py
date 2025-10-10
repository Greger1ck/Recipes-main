from django.urls import path
from django.conf.urls.static import static

from cooking import settings
from recipes.views import IndexPage, RecipeDetailPage, SearchPage, CategoryList

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('recipe/<slug:slug>/', RecipeDetailPage.as_view(), name='recipe'),
    path('search', SearchPage.as_view(), name='search'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
]
