from django.conf.urls import patterns, url
from tasks import views

urlpatterns = patterns('',
    # ex: /tasks/
    url(r'^(?P<status>(today|someday|fixed))/$', views.index, name='index'),
    # ex: /tasks/5/
    url(r'^(?P<task_id>\d+)/detail/$', views.detail, name='detail'),
    # ex: /tasks/5/results/
    url(r'^(?P<task_id>\d+)/results/$', views.results, name='results'),

    url(r'^add_task_form/$', views.add_task_form, name='add_task_form'),
    url(r'^do_action/$', views.do_action, name='do_action'),
)