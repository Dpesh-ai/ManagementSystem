# Register your models here.
from django.contrib import admin
from .models import Project, ProjectData, Client

admin.site.register(Project)
admin.site.register(ProjectData)
admin.site.register(Client)