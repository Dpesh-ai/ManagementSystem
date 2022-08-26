from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

    class Meta:
        model = Todo 
        fields = '__all__'

        labels = {
            "todo_name": "Todo Item",
            "only_admin": "Admin Restrcitons"
        }

        widgets = {
            "todo_name": forms.TextInput(attrs={'placeholder': 'e.g. Interns Task', 'class': 'form-control p-3 mb-3'}),
        }

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'deadline':
                self.fields[field].widget.attrs.update({'class': 'form-control p-3 mb-3'})

    class Meta:
        model = Todo_data
        fields = '__all__'
        exclude = ['completed', 'todo']
        
        labels = {
            "task": "Tasks Name",
            "task_type": "Select Task Type",
            "priority": "Select Priority",
            "assigned_to": "Select Asignee",
            "deadline": "Select a deadline"
        }

        widgets = {
            "task": forms.TextInput(attrs={'placeholder': 'e.g. We need to plant a tree.'}),
            "deadline": forms.SelectDateWidget(),
            # "task_type": forms.ChoiceField(attrs={}),
            # "priority": forms.ChoiceField(attrs={}),
            # "asiggned_to": forms.ChoiceField(attrs={}),
            # "deadline":forms.DateTimeField(attrs={}),

        }