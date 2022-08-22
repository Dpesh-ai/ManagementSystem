from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Todo)
admin.site.register(Todo_data)
admin.site.register(Task_category)
