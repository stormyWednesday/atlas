from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.projects.models import Module
from apps.projects.forms import ProjectForm




# Create your views here.


class ProjectListView(ListView):
    model = Module
    template_name = 'project/list.html'
    context_object_name = 'project_obj'



class ProjectCreateView(CreateView):
    model = Module
    form_class = ProjectForm
    template_name = 'project/create.html'
    context_object_name = 'project_obj'
    success_url = reverse_lazy('projects:project-list')


class ProjectDelete(DeleteView):
    model = Module
    template_name = 'project/delete.html'
    context_object_name = 'project_obj'
    success_url = reverse_lazy('projects:project-list')


class ProjectUpdate(UpdateView):
    model = Module
    form_class = ProjectForm
    template_name = 'project/update.html'
    context_object_name = 'project_obj'
    success_url = reverse_lazy('projects:project-list')





















    






