from django import forms

class TasksForm(forms.Form):
    task_title = forms.CharField()
    deadline_date = forms.DateField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass