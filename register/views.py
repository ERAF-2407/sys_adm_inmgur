
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Register
from .forms import RegisterForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('registers')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o Contraseña Incorrecto."})

        login(request, user)
        return redirect('registers')

@login_required
def registers(request):
    registers = Register.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'registers.html', {"registers": registers})

@login_required
def registers_completed(request):
    registers = Register.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'registers.html', {'registers': registers})

@login_required
def create_register(request):
    if request.method == "GET":
        return render(request, 'create_register.html', {"form": RegisterForm})
    else:
        try:
            form = RegisterForm(request.POST)
            new_register = form.save(commit=False)
            new_register.user = request.user
            new_register.save()
            return redirect('registers')
        except ValueError:
            return render(request, 'create_register.html', {"form": RegisterForm, "error": "Error creando registro."})

@login_required
def register_detail(request, register_id):
    if request.method == 'GET':
        register = get_object_or_404(Register, pk=register_id, user=request.user)
        form = RegisterForm(instance=register)
        return render(request, 'register_detail.html', {'register': register, 'form': form})
    else:
        try:
            register = get_object_or_404(Register, pk=register_id, user=request.user)
            form = RegisterForm(request.POST, instance=register)
            form.save()
            return redirect('registers')
        except ValueError:
            return render(request, 'register_detail.html', {'register': register, 'form': form, 'error': "Error cargando registro"})

@login_required
def complete_register(request, register_id):
    register = get_object_or_404(Register, pk=register_id, user=request.user)
    if request.method == 'POST':
        register.datecompleted = timezone.now()
        register.save()
        return redirect('registers')

@login_required
def delete_register(request, register_id):
    register = get_object_or_404(Register, pk=register_id, user=request.user)
    if request.method == 'POST':
        register.delete()
        return redirect('registers')

@login_required
def signout(request):
    logout(request)
    return redirect('home')


