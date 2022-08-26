from django.shortcuts import render, redirect
from .models import Project, ProjectData, Client
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login-page')
def project_detail(request, pk):
    context = {}
    currentProject = Project.objects.get(id=pk)
    detail = ProjectData.objects.filter(project=currentProject)
    context['detail'] = detail
    context['pk'] = pk
    return render(request, 'project/project_detail.html', context)

@login_required(login_url='login-page')
def project(request):
    return render(request, 'project/project.html')

@login_required(login_url='login-page')
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')

    context = {}
    context['form'] = form
    return render(request, 'project/create_project.html', context)

@login_required(login_url='login-page')
def create_task(request, pk):
    form = TaskForm()
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        # print(request.POST)
        ProjectData.objects.create(
            project = project,
            remarks = request.POST.get('remarks'),
            client_name = Client.objects.get(pk=request.POST['client_name']),
            data = request.POST.get('data'),
        )
        return redirect('project_detail', pk)
    context = {}
    context['form'] = form
    context['pk'] = pk
    return render(request, 'project/create_task.html', context)


@login_required(login_url='login-page')
def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk)
    
    context = {}
    context['form'] = form
    context['pk'] = pk

    return render(request, 'project/edit_project.html', context)


def currentLog(status):
    data = {"backlog": False,
            "todo": False,
            "dev_started": False,
            "dev_completed": False,
            "review_started": False,
            "review_done": False,
            "closed": False
            }

    if status == 0:
        data["backlog"] = True
    elif status == 1:
        data["todo"] = True
    elif status == 2:
        data["dev_started"] = True
    elif status == 3:
        data["dev_completed"] = True
    elif status == 4:
        data["review_started"] = True
    elif status == 5:
        data["review_done"] = True
    elif status == 7:
        data["closed"] = True

    return data

@login_required(login_url='login-page')
def edit_project_detail(request, pk, status, detail_id):
    project_data = ProjectData.objects.get(id=detail_id)
    currentLog_data = currentLog(status)

    for key, value in currentLog_data.items():
        setattr(project_data, key, value)

    project_data.save()

    return redirect('project_detail', pk)

@login_required(login_url='login-page')
def delete_data(request, pk, project_id):
    data = ProjectData.objects.get(id=pk)

    data.delete()
    return redirect('project_detail', project_id)

@login_required(login_url='login-page')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    return render(request, 'project/delete.html', {'obj': project})
