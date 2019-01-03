from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.


class ProjectListView(TemplateView):
    template_name = 'project/list.html'


class ProjectCreateView(TemplateView):
    template_name = 'project/create.html'
