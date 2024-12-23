from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import User

from .forms import ProjectForm
from .models import Project, Employee, Client, Task

def home(request):
    num_projects = Project.objects.count()
    num_employee = Employee.objects.count()
    num_clients = Client.objects.count()
    num_tasks = Task.objects.count()

    if request.user.is_authenticated:
        user_projects = Project.objects.filter(manager=request.user)
    else:
        user_projects = []

    return render(request, 'index.html', {
        'num_projects': num_projects,
        'num_employee': num_employee,
        'num_clients': num_clients,
        'num_tasks': num_tasks,
        'user_projects': user_projects,
    })

def user_projects(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(manager=request.user)
    else:
        projects = []

    return render(request, 'user_projects.html', {'projects': projects})

def projects(request):
    paginator = Paginator(Project.objects.all(), 4)
    page_number =request.GET.get('page')
    projects = paginator.get_page(page_number)
    return render(request, 'projects.html', {'projects': projects})
    # projects = Project.objects.all()
    # return render(request, 'projects.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project.html', {'project': project})

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee.html', {'employee': employee})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def client_detail(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'client.html', {'client': client})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    project = task.project_tasks.first() if task.project_tasks.exists() else None
    employees = project.employees.all() if project else []
    return render(request, 'task.html', {'task': task, 'project': project, 'employees': employees})

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # Pridedame request.FILES
        if form.is_valid():
            project = form.save(commit=False)
            project.manager = request.user
            project.save()
            form.save_m2m()  # išsaugoti darbuotojų ManyToManyField ryšius
            return redirect('user_projects')
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})
