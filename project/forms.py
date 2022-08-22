from django.forms import ModelForm
from .models import Project, ProjectData

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = ProjectData
        fields = ['remarks', 'client_name', 'data']