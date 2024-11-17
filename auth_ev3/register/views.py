from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, LoginForm
import requests

# Create your views here.
def register(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        #procesos del formulario
        pass
    return render(request, 'register.html', {'form':form})

def home(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        #proceso de login
        pass
    return render(request, 'home.html', {'form':form})

@login_required
def dashboard(request):
    user_id = request.user.id
    try:
        response = requests.get(f'http://localhost:8000/api/users/{user_id}')
        if response.status_code == 200:
            user_data = response.json()
            welcome_message = f"Bienvenido {user_data['username']}"
        else:
            welcome_message = "Error al obtener los datos del usuario"
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        welcome_message = "Error al obtener los datos del usuario"

    return render(request, 'dashboard.html', {'welcome_message': welcome_message})