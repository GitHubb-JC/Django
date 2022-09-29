from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def index(request):
    todo_ = todo.objects.all()
    content = {
        "todo_": todo_,
    }
    return render(request, "todo/index.html", content)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect("todo:index")


def delete(request, todo_pk):
    todo_ = todo.objects.get(pk=todo_pk)
    todo_.delete()
    return redirect("todo:index")


def update(request, todo_pk):
    todo_ = todo.objects.get(pk=todo_pk)
    if todo_.completed == 1:
        todo_.completed = 0
    elif todo_.completed == 0:
        todo_.completed = 1
    todo_.save()
    return redirect("todo:index")
