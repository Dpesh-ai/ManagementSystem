# Register your models here.
from django.contrib import admin
from .models import Project, ProjectData

admin.site.register(Project)
admin.site.register(ProjectData)