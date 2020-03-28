
from django.urls import path
from todos import views

urlpatterns = [
    path('', views.todo, name='todo'), 
    path('update-todo/<int:todo_id>', views.update_todo, name='update_todo'), 
    path('delete-todo/<int:todo_id>', views.delete_todo, name='delete_todo'), 
  
]