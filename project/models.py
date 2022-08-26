from django.db import models

# Create your models here.

class  Project(models.Model):
    project_name = models.CharField(max_length=500, unique=True)
    # project_data = models.JSONField()
    only_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name

    # class Meta:
    #     ordering = ['-date_created']


class Client(models.Model):
    client_name = models.CharField(max_length=500)
    client_address = models.CharField(max_length=500)
    client_contact = models.CharField(max_length=500)
    remarks = models.CharField(max_length=500, blank=True)
    year_of_work = models.DateTimeField()


    def __str__(self):
        return self.client_name



class ProjectData(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_name = project.name
    backlog = models.BooleanField(default=True)
    todo = models.BooleanField(default=False)
    dev_started = models.BooleanField(default=False)
    dev_completed = models.BooleanField(default=False)
    review_started = models.BooleanField(default=False)
    review_done = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    data = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data[:50]

    