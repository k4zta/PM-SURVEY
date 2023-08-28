from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib import messages


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {username}!')
            return redirect('estudiante/')
        else:
            error_msg = "Usuario o contraseña incorrectos"
            return render(request, 'home.html', {'error_msg': error_msg})

    return render(request, 'home.html')


def estudiante(request):
    user = request.user
    return render(request, "estudiante.html", {'nombre': user.first_name})
