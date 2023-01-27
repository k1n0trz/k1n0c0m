from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ServicioForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'El usuario ya existe'
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Resgistro de usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mis-servicios')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'El password no coincide'
        })


def misservicios(request):
    return render(request, 'mis-servicios.html')

def solicitar(request):
    if request.method == 'GET':
        return render(request, 'solicitud.html', {
            'form': ServicioForm
        })
    else:
        print(request.POST)
        return render(request, 'solicitud.html', {
            'form': ServicioForm
        })

def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                     password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o el password está incorrecto'
            })
        else:
            login(request, user)
            return redirect('mis-servicios')

