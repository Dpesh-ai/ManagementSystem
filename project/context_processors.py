from .models import Project

def project_processor(request):
    return {"projects": Project.objects.all()}