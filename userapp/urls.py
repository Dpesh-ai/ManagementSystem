from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('login-page', views.loginPage, name='login-page'),
     path('home-page', views.home, name='home-page'),
     path('logout', views.logoutUser, name='logout'),
]
