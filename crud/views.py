from django.shortcuts import render, redirect
from django.views import View
from .models import TaskModel

# Create your views here.

class ReadTaskView(View):
    def get(self, request):
        tasks = TaskModel.objects.all()
        context = {
            "tasks":tasks,
        }
        return render(request, "crud.html", context)

class CreateTaskView(View):
    def get(self, request):
        return render(request, "task_form.html")
    
    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        is_completed = request.POST.get("is_completed") == 'on'

        TaskModel.objects.create(
            title=title,
            description=description,
            is_completed=is_completed,
        )

        return redirect("read_tasks")

class DeleteTaskView(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        task = TaskModel.objects.get(id=id)
        task.delete()
        return redirect("read_tasks")

class UpdateTaskView(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        task = TaskModel.objects.get(id=id)
        context = {
            "task":task,
        }
        return render(request, "task_form.html", context)
    
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        task = TaskModel.objects.get(id=id)
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.is_completed = request.POST.get("is_completed") == 'on'
        task.save()
        
        return redirect("read_tasks")


