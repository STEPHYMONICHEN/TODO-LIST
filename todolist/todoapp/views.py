from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.order_by('created_at')
    form = TodoForm()
    return render(request, 'tasklist.html', {'todos': todos, 'form': form})


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(title=request.POST['title'])
        new_todo.save()
    return redirect('todo_list')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')


def delete_todo(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return redirect('todo_list')


def edit_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'editlist.html', {'form': form, 'todo_id': todo_id})

