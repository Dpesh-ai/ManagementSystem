from django.forms import ModelForm
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = Todo 
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Todo_data
        fields = '__all__'
        exclude = ['completed', 'todo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs.update({"type": 'password'})