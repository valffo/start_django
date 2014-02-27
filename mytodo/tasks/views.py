from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from tasks.models import Task
from datetime import date
from django.shortcuts import render, get_object_or_404

# Create your views here.
STATUSES = ('today', 'someday', 'fixed')

def index(request, status):

    print(status)
    if status == 'today':
        latest_tasks_list = Task.objects.filter(deadline_date = date.today()).order_by('-deadline_date')[:5]
    elif status == 'fixed':
        latest_tasks_list = Task.objects.filter(done=1).order_by('-deadline_date')[:5]
    elif status == 'fixed':
        latest_tasks_list = Task.objects.filter(done=1).order_by('-deadline_date')[:5]
    else:
        latest_tasks_list = Task.objects.all().order_by('-deadline_date')[:5]
    template = loader.get_template('tasks/index.html')
    context = RequestContext(request, {
        'latest_tasks_list': latest_tasks_list,
        'status': status,
        'statuses': STATUSES
    })
    return HttpResponse(template.render(context))

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

def results(request, task_id):
    return HttpResponse("You're looking at the results of poll %s." % task_id)

def vote(request, task_id):
    return HttpResponse("You're voting on poll %s." % task_id)