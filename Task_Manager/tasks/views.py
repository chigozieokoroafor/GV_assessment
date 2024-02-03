from django.shortcuts import render, redirect, resolve_url
from .models import Task
from django.contrib.auth.decorators import login_required
from datetime import datetime

status = {
    True:"Completed",
    False:"Pending"
}

# Create your views here.
def index(request):
    return render(request, "base.html")

def home(request):
    return redirect("task_route")

@login_required
def my_task(request):
    # if request.method == "POST":
    #     pass
    user = request.user
    if user.is_authenticated:
        
            # title = request.POST["title"]

        tasks = Task.objects.filter(user=user)
        
        return render(request, "my_tasks.html", {
            "tasks":tasks
        })

@login_required
def spec_task(request, pk):
    task =  Task.objects.get(pk=pk)
    if request.method == "PUT":
        task.completed = True
        task.save()
        return redirect
    
    return render(request, "update.html", {
        "task":task,
        "due_date":str(task.due_date)
        
    })

@login_required
def upload_view(request):
    user = request.user
    if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            due_date = request.POST["due_date"]
            task = Task.objects.create(title=title,
                                description=description,
                                due_date = due_date,
                                user = user)
            task.save()
            return redirect("task_route")

    return render(request, "add_tasks.html")

@login_required
def mark_completed(request, pk):
    user = request.user
    task = Task.objects.get(pk=pk, user=user)
    if task.status == "pending":
        task.status = "completed"
    else:
        task.status = "pending"
    task.save()
    return redirect("task_route")

def delete_task(request, pk):
    user = request.user
    task = Task.objects.get(pk=pk, user=user)
    task.delete()
    return redirect("task_route")
