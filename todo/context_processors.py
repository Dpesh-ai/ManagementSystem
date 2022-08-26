from .models import Todo

def todo_processor(request):
    return {"todo":Todo.objects.all()}