from django import forms

from apps.projects.models import Module


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'
