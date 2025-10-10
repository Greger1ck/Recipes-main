from django.urls import path
from django.conf.urls.static import static

from cooking import settings
from recipes.views import CustomLoginView, CustomLogoutView, IndexPage, RecipeDetailPage, RegisterView, SearchPage, CategoryList

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('recipe/<slug:slug>/', RecipeDetailPage.as_view(), name='recipe'),
    path('search', SearchPage.as_view(), name='search'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('login', CustomLoginView.as_view(), name= 'my_login'),
    path('reg', RegisterView.as_view(), name= 'reg'),
    path('logout', CustomLogoutView.as_view(), name= 'my_logout'),
]
