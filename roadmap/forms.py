from django import forms

from .models import Goal, Task


class CustomDateInput(forms.DateInput):
    input_type = 'date'


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'deadline']
        widgets = {
            'deadline': CustomDateInput()
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
