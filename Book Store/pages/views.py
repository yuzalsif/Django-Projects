from django.shortcuts import render
from django.views.generic import TemplateView

# The home page view.

class HomePageView(TemplateView):
    template_name = 'index.html'
