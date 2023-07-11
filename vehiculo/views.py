from tokenize import PseudoExtras

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import (HttpResponseRedirect, render)

from .forms import UserRegisterForm
from .models import Vehiculo


# Create your views here.
def index_view(request):
    template_name = 'index.html'
    return render(request, template_name)

@permission_required(perm='visualizar_catalogo', login_url='/vehiculo/login')
def listado_view(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, 'listado.html', context)


@login_required(login_url='/vehiculo/login')
@permission_required(perm='vehiculo.can_add_vehiculo', login_url='/vehiculo/login')
def add(request):
    return render(request, 'agregar_vehiculo.html')


def addvehiculo(request):
    marca = request.POST['marca']
    modelo = request.POST['modelo']
    s_carroceria = request.POST['s_carroceria']
    s_motor = request.POST['s_motor']
    categoria = request.POST['categoria']
    precio = request.POST['precio']

    vehiculo = Vehiculo(marca=marca, modelo=modelo, s_carroceria=s_carroceria,
                        s_motor=s_motor, categoria=categoria, precio=precio)
    vehiculo.save()
    return HttpResponseRedirect('/vehiculo/add')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type
            )
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)
            if form.cleaned_data['can_add_vehiculo']:
                permission = Permission.objects.get(
                    codename='can_add_vehiculo')
                user.user_permissions.add(permission)
                user.is_superuser = True
                user.is_staff = True
                user.save()

            login(request, user)
            messages.success(request, "Usuario registrado satisfactoriamente.")
        else:
            messages.error(
                request, "Registra invalido. Algunos de los datos ingresados no son correctos.")
        return HttpResponseRedirect("/")

    form = UserRegisterForm()
    context = {"register_form": form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Username o password incorrectos.')
                return HttpResponseRedirect('/vehiculo/login')
        else:
            messages.error(request, 'Username o password incorrectos.')
            return HttpResponseRedirect('/vehiculo/login')
    form = AuthenticationForm()
    context = {'login_form': form}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado su sesión satisfactoriamente.")
    return HttpResponseRedirect('/')
