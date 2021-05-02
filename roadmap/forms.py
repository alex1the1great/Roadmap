from django import forms

from .models import Goal


class CustomDateInput(forms.DateInput):
    input_type = 'date'


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'deadline']
        widgets = {
            'deadline': CustomDateInput()
        }

