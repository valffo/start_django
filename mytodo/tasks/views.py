from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from datetime import date
from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from models import Task
from forms import TasksForm
from django.views import generic
from django.core.urlresolvers import reverse

from django.conf.urls import patterns, url
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def index(request, status):

    STATUSES = ['today', 'someday', 'fixed']
    if status == 'today':
        latest_tasks_list = Task.objects.filter(deadline_date=date.today(), user=request.user.id).order_by('-deadline_date')[:5]
    elif status == 'fixed':
        latest_tasks_list = Task.objects.filter(done=1, user=request.user.id).order_by('-deadline_date')[:5]
    else:
        latest_tasks_list = Task.objects.filter(user=request.user.id).order_by('-deadline_date')[:5]
    template = loader.get_template('tasks/index.html')
    context = RequestContext(request, {
        'latest_tasks_list': latest_tasks_list,
        'status': status,
        'statuses': STATUSES,
        'userg': str(request.user.id) + '   ' + request.user.username
    })
    return HttpResponse(template.render(context))

@login_required
def add(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = TasksForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            task = Task(
                deadline_date=request.POST['deadline_date'],
                task_title=request.POST['task_title'],
                user_id=request.user.id,
            )
            task.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'pk': task.id, }))
    else:
        form = TasksForm() # An unbound form

    return render(request, 'tasks/add.html', {'form': form, })

def do_action(request):
    pass

class DetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'
