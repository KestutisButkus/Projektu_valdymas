from . import views
from django.urls import path
from .views import home

urlpatterns = [
    path('', views.home, name='home'),  # Numatytasis kelias promgt programos pagrindiniam puslapiui
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('employees/', views.employees, name='employees'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
    path('clients/', views.clients, name='clients'),
    path('client/<int:id>/', views.client_detail, name='client_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('register/', views.register, name='register'),
    path('user_projects/', views.user_projects, name='user_projects'),
    path('create_project/', views.create_project, name='create_project'),
]
