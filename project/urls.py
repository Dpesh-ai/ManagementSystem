from django.urls import path
from . import views

from .views import (
    project,
    create_project,
    edit_project_detail,
)

# app_name = "project"
urlpatterns = [

    # homepage - page that displays list of project
    path('project/', project, name='project'),


    path('project/create_project/', create_project, name='create_project'),

    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    
    # edit project status (eg. backlog to remarks)
    path('project/<int:pk>/edit/shift_to/<int:status>/<int:detail_id>', edit_project_detail, name='edit_project_detail'),


    path('project/create_task/<int:pk>/', views.create_task, name='create_project_task'),
    path('project/<int:pk>/edit', views.edit_project, name='edit_project'),
    path('delete_data/<int:pk>/<int:project_id>', views.delete_data, name='delete_data'),
    path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
    
]