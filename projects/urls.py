from django.urls import path
from . import views




urlpatterns = [
    # path('projects/', views.projects,name="projects"), # for  run by particular path
    path('', views.projects,name="projects"),  #For making home page default path which we want , empty string means this is going to our domain
    path('project/<str:pk>/', views.project,name="project"),
]

