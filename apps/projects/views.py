from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy

from apps.projects.models import Module
from apps.projects.forms import ProjectForm

# Create your views here.


class ProjectListView(TemplateView):
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = Module
    form_class = ProjectForm
    template_name = 'project/create.html'
    context_object_name = 'project_obj'
    success_url = reverse_lazy('projects:project-list')

