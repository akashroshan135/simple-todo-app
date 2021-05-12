from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        labels = {'name' : ''}
        model = Task
        fields = ['name']