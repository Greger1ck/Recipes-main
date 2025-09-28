from django.shortcuts import render
from django.views.generic import (
    ListView,

)
class IndexPage(ListView):
    template_name = ''
    model = ''
    