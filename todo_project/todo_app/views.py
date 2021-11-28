from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .form import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListView(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

class DetailListView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class UpdateListView(UpdateView):
    model=Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        url = reverse_lazy("todo_app:detail",kwargs={'pk':self.object.id})
        return url


class DeleteListView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_app:taskview')


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()


    return render(request,'home.html',{'task1':task1})


def delete(request,taskid):
    task_id=Task.objects.get(id=taskid)
    if request.method=='POST':
        task_id.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task_id = Task.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task_id})