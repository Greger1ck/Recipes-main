
from django.urls import path
from django.conf.urls.static import static

from cooking import settings
from recipes.views import IndexPage

urlpatterns = [
    path('',IndexPage.as_view(), name = "home"),

]
