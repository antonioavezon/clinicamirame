from sqlite3 import IntegrityError
import traceback
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import LoginForm, RegisterForm
import logging


logger = logging.getLogger('django')
app_logger = logging.getLogger('app_logger')

@csrf_protect
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  # Usamos el formulario de login
        if form.is_valid():  # Validamos la entrada
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f"Inicio de sesión exitoso para el usuario: {username}")
                return redirect('welcome')
            else:
                logger.warning(f"Intento de inicio de sesión fallido para el usuario: {username}")
                form.add_error(None, "Usuario o contraseña incorrectos.")
    else:
        form = LoginForm()  # Si es un GET, mostramos el formulario vacío
    return render(request, 'login.html', {'form': form})

@csrf_protect
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                # Intentamos crear el usuario
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Autenticar y loguear al usuario
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('welcome')
            except IntegrityError:
                form.add_error('username', 'El nombre de usuario ya existe.')
        else:
            form.add_error(None, 'Datos del formulario no son válidos.')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

@csrf_protect
def welcome(request):
    return render(request, 'welcome.html')

@csrf_protect
def error_escritura(request):
    try:
        raise IOError("Error de escritura simulado")
    except Exception as e:
        error_message = str(e)
        error_traceback = traceback.format_exc().splitlines()[-1]  
        app_logger.error(f"ERROR: {error_message}") 
        app_logger.error(f"Traceback: {error_traceback}")  
        return HttpResponse(f"Se ha producido un error de escritura: {error_message}")

@csrf_protect
def error_sistema(request):
    try:
        raise SystemError("Error de sistema simulado")
    except Exception as e:
        error_message = str(e)
        error_traceback = traceback.format_exc().splitlines()[-1]
        app_logger.error(f"ERROR: {error_message}")  
        app_logger.error(f"Traceback: {error_traceback}")  
        return HttpResponse(f"Se ha producido un error de sistema: {error_message}")
    
@csrf_protect
def user_logout(request):
    username = request.user.username 
    logout(request)
    logger.info(f"Cierre de sesión exitoso para el usuario: {username}")  # Guardar el cierre de sesión en los logs
    return redirect('login')