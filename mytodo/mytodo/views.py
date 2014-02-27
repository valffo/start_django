from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from tasks.models import Task
from datetime import date
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):

    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))
