from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    date_to_begin = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Task
        fields = ['todo_item', 'date_to_begin']

