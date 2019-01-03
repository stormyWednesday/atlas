from django.urls import path

from apps.projects import views

app_name = 'projects'

urlpatterns = [
    path('project/list/', views.ProjectListView.as_view(), name='project-list'),
]
