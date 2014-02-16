from django.contrib import admin
from tasks.models import Task


class TaskInline(admin.TabularInline):
    pass
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    # ...
    list_display = ('task_title', 'user', 'deadline_date', 'done',)
    list_filter = ['user', 'done']
    search_fields = ['task_title']
admin.site.register(Task, TaskAdmin)