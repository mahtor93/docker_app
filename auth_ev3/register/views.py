from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm

# Create your views here.
def register(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        #procesos del formulario
        pass
    return render(request, 'register.html', {'form':form})