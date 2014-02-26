from django.conf.urls import patterns, url
from tasks import views

urlpatterns = patterns('',
    # ex: /tasks/
    url(r'^(?P<status>(today|someday|fixed))/$', views.index, name='index'),
    # ex: /tasks/5/
    url(r'^(?P<task_id>\d+)/detail/$', views.detail, name='detail'),
    # ex: /tasks/5/results/
    url(r'^(?P<task_id>\d+)/results/$', views.results, name='results'),
    # ex: /tasks/5/vote/
    url(r'^(?P<task_id>\d+)/vote/$', views.vote, name='vote'),
)