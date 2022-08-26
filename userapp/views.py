from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

def index(request):
    return render(request, 'initial_page.html')

def home(request):
    return render(request, 'index.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'Username or password doesnot match')


    return render(request, 'userapp/login-page.html')

def logoutUser(request):
    logout(request)
    return redirect('index')