from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404


@csrf_exempt
def add_todo(request):
    content = request.POST.get('content')
    added_date = timezone.now()
    Todo.objects.create(added_date=added_date, text=content)
    print(content)
    return redirect(tasks_todo)

@csrf_exempt
def tasks_todo(request):
    tasks = Todo.objects.order_by('-added_date')
    context = {'tasks': tasks}
    return render(request, 'todo_app/todo_list.html', context)


@csrf_exempt
def delete_task(request, id):
    print('im here')
    t = get_object_or_404(Todo, pk=id)

    if request.method == 'POST':
        t.delete()
    return redirect(tasks_todo)


@csrf_exempt
def detail_task(request, id):
    task = get_object_or_404(Todo, pk=id)
    if task:
        context = {'task': task}
        return render(request, 'todo_app/detail_task.html', context)

    return redirect(tasks_todo)

@csrf_exempt
def update_task(request, id):
    new_content = request.POST.get('update_content')
    edit_date = timezone.datetime.now()
    t = Todo.objects.get(pk=id)
    t.text = new_content
    t.save(update_fields=['text'])
    return redirect(tasks_todo)