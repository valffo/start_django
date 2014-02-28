from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from datetime import date
from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404, render_to_response

from tasks.models import Task
from tasks.forms import TasksForm
from django.views.generic.edit import FormView

# Create your views here.

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

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

def results(request, task_id):
    return HttpResponse("You're looking at the results of poll %s." % task_id)

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = TasksForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = TasksForm() # An unbound form

    return render(request, 'tasks/add.html', {
        'form': form,
    })

def form_valid(self):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.send_email()
    return super(ContactView, self).form_valid(form)

def do_action(request):
    pass

def add_task_form(request, task_id=0, user_name = None):
    if (task_id):
        taskObj = Task.objects.get(pk=task_id)
    TaskFormSet = modelformset_factory(Task)
    if request.method == "POST":
        formset = TaskFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect('/tasks')
    else:
        #user = User.objects.get(name=user_name)
        #formset = TaskFormSet(instance=user)
        formset = TaskFormSet()
    return render_to_response("tasks/new.html", {
        "formset": formset,
    })