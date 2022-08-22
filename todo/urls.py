from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.todo, name='todo'),
    path('create_todo', views.create_todo, name='create_todo'),
    path('todo_details/<int:pk>/', views.todo_details, name='todo_details'),
    path('create_task/<int:pk>/', views.create_task, name='create_task'),
    path('edit_task/<int:pk>/<int:todo_id>/', views.edit_task, name='edit_task'),
    path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('todo_details/<int:todo_id>/delete_task/<int:pk>/', views.delete_task_data, name='delete_task_data'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('task_completed/<int:todo_id>/<int:task_id>/', views.task_completed, name='task_completed'),
    

]
