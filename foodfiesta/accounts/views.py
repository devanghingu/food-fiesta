from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Index(TemplateView):
    '''template for display when user come'''
    template_name="frontend/index.html"
