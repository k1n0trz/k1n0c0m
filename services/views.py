from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ServicioForm, SolicitudForm
from .models import Servicio, Solicitud
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def privacidad(request):
    return render(request, 'politica-privacidad.html')

def cookies(request):
    return render(request, 'politica-cookies.html')

def diseno(request):
    return render(request, 'servicios/diseno.html')

def desarrollo(request):
    return render(request, 'servicios/desarrollo.html')

def marketing(request):
    return render(request, 'servicios/marketing.html')

def produccion(request):
    return render(request, 'servicios/produccion.html')

def eventos(request):
    return render(request, 'servicios/eventos.html')

def blockchain(request):
    return render(request, 'servicios/blockchain.html')

def solicitud(request):
    if request.method == 'GET':
        return render(request, 'success.html', {
            'form': SolicitudForm,
        })
    else:
        try:
            form = SolicitudForm(request.POST)
            new_solicitud = form.save(commit=False)
            new_solicitud.save()
            return redirect('solicitud')
        except ValueError:
            return render(request, 'success.html', {
                'form': SolicitudForm,
                'error': 'Por favor ingrese datos válidos'
            })


def contacto(request):
    return render(request, 'contacto.html')

def servicios(request):
    return render(request, 'servicios.html')

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

@login_required
def misservicios(request):
    servicios = Servicio.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'mis-servicios.html', {'servicios': servicios})

@login_required
def servicios_completados(request):
    servicios = Servicio.objects.filter(user=request.user, datecompleted__isnull=False).order_by
    ('-datecompleted')
    return render(request, 'mis-servicios.html', {'servicios': servicios})

@login_required
def servicio_detalle(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Servicio, pk=servicio_id, user=request.user)
        form = ServicioForm(instance=servicio)
        return render(request, 'myservicio-detalle.html', {'servicio': servicio, 'form': form})
    else:
        try:
            servicio = get_object_or_404(Servicio, pk=servicio_id, user=request.user)
            form = ServicioForm(request.POST, instance=servicio)
            form.save()
            return redirect('mis-servicios')
        except ValueError:
            return render(request, 'myservicio-detalle.html', {'servicio': servicio, 'form': form, 'error': 'Error actualizando servicio'})

@login_required
def complete_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id, user=request.user)
    if request.method == 'POST':
        servicio.datecompleted = timezone.now()
        servicio.save()
        return redirect('mis-servicios')

@login_required
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id, user=request.user)
    if request.method == 'POST':
        servicio.delete()
        return redirect('mis-servicios')

@login_required
def solicitar(request):
    if request.method == 'GET':
        return render(request, 'cotizacion.html', {
            'form': ServicioForm
        })
    else:
        try:
            form = ServicioForm(request.POST)
            new_servicio = form.save(commit=False)
            new_servicio.user = request.user
            new_servicio.save()
            return redirect('mis-servicios')
        except ValueError:
            return render(request, 'cotizacion.html', {
                'form': ServicioForm,
                'error': 'Por favor ingrese datos válidos'
            })

@login_required
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

