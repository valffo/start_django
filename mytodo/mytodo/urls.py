from django.conf.urls import patterns, include, url
from django.conf import settings
from registration.forms import RegistrationFormUniqueEmail
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    url(r'^accounts/', include('registration.urls')),
    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    url(r'^$', 'mytodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
)
