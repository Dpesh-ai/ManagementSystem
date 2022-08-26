from django import forms
from .models import Project, ProjectData

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control p-3 mb-3'})

    class Meta:
        model = ProjectData
        fields = ['data',  'client_name', 'remarks']
        
        labels = {
            "remarks": "Remarks",
            "client_name": "Client Name",
            "data": "Task Name",
        }

        widgets = {
            "remarks": forms.Textarea(attrs={'placeholder': 'e.g. Remarks'}),
            # "client_name": forms.ChoiceField(),
            "data": forms.TextInput(attrs={'placeholder': 'e.g. Design Product Page'}),
        }




class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

    class Meta:
        model = Project
        fields = '__all__'
        
        labels = {
            "project_name": "Project Name",
            "only_admin": "Acess Restriction",
        }

        widgets = {
            "project_name": forms.TextInput(attrs={'placeholder': 'e.g. Distributed Ecommerce', 'class': 'form-control p-3 mb-3'}),
        }


