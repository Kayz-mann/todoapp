from django.shortcuts import render, redirect
from todos.forms import TodoForm
from django.contrib.auth.models import User
from todos.models import Todo
from django.contrib import messages

# Create your views here.

def todo(request):
  uid = int(request.user.id)
  if request.method == "GET":
    todos = Todo.objects.filter(user__id=uid)
    context = {
      "todos":todos,
    }
    return render(request, "todos/todos.html", context)
    
  if request.method == "POST":
    todos = Todo.objects.filter(user__id=uid)
    uid = int(request.user.id)
    print(uid)
    form = TodoForm(request.POST)
    if form.is_valid():
      add_todo = form.save(commit=False)
      add_todo.description = form.cleaned_data['description']
      add_todo.user = User(pk=uid)
      add_todo.save()
      messages.success(request, "Todo created successfully")
      return redirect("todo")
    else:
      context = {
        "form":form,
         "todos":todos,
        
      }
      return render(request, "todos/todos.html", context)
    

def update_todo(request, todo_id):
  if request.method == "POST":
    form = TodoForm(request.POST)
    if form.is_valid():
      update_todo = Todo.objects.get(pk=todo_id)
      update_todo.description = form.cleaned_data['description']
      update_todo.save()
      messages.success(request, "Todo updated successfully")
      return redirect("todo")
    else:
      messages.success(request, "Oops, Something went wrong")
      return redirect("todo")
  else:
    return redirect("todo")


def delete_todo(request, todo_id):
  if request.method == "POST":
    delete_todo = Todo.objects.get(pk=todo_id)
    delete_todo.delete()
    messages.success(request, "Todo deleted successfully")
    return redirect("todo")
  else:
    messages.success(request, "Error deleting your todo")
    return redirect("todo")

      



