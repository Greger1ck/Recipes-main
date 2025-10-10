from django.urls import path
from django.conf.urls.static import static

from cooking import settings
from recipes.views import IndexPage, RecipeDetailPage

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('recipe/<slug:slug>/', RecipeDetailPage.as_view(), name='recipe'),
]
