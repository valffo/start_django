from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=200)
    deadline_date = models.DateField()
    done = models.BooleanField(default=False)
    user  = models.ForeignKey(User)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'