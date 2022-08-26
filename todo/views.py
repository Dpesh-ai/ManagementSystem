from django.shortcuts import render, redirect
from .models import Todo, Todo_data, Task_category
from .forms import TaskForm, TodoForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login-page')
def todo(request):
    return render(request, 'todo/todo.html')

@login_required(login_url='login-page')
def create_todo(request):
    form = TodoForm()

    if request.method == 'POST':
        # print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    context = {}
    context['form'] = form
    return render(request, 'todo/create_todo.html', context)

@login_required(login_url='login-page')
def todo_details(request, pk):
    context = {}
    currentTodo = Todo.objects.get(id=pk)
    detail = Todo_data.objects.filter(todo=currentTodo)
    context['detail'] = detail
    context['pk'] = pk
    return render(request, 'todo/todo_detail.html', context)

@login_required(login_url='login-page')
def create_task(request, pk):
    form = TaskForm()
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.todo = todo
            data.save()

            return redirect('todo_details', pk)
    context = {}
    context['form'] = form
    context['pk'] = pk
    return render(request, 'todo/create_task.html', context)

@login_required(login_url='login-page')
def edit_task(request, pk, todo_id):
    context = {}
    todo = Todo_data.objects.get(id = pk)
    form = TaskForm(instance=todo)
    context['form'] = form
    if request.method == "POST":
        form = TaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo_details', todo_id)

    return render(request, 'todo/edit.html', context)

@login_required(login_url='login-page')
def edit_todo(request, pk):
    context = {}
    todo = Todo.objects.get(id = pk)
    form = TodoForm(instance=todo)
    context['form'] = form
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo_details', pk)

    return render(request, 'todo/edit.html', context)


@login_required(login_url='login-page')
def delete_task_data(request, todo_id, pk):
    data = Todo_data.objects.get(id = pk)
    data.delete()
    return redirect('todo_details', todo_id)


@login_required(login_url='login-page')
def delete_todo(request, pk):
    todo = Todo.objects.get(id = pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')
    return render(request, 'todo/delete.html', {'obj':todo})

@login_required(login_url='login-page')
def task_completed(request, todo_id, task_id):
    data = Todo_data.objects.get(id=task_id)
    if data.completed == True:
        data.completed = False
    else:
        data.completed = True
    data.save()
    return redirect('todo_details', todo_id)
    