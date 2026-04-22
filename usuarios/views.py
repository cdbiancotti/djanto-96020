from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import FormularioDeAutenticacion, FormularioCreacion, FormularioEdicion
from django.contrib.auth.decorators import login_required

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = FormularioDeAutenticacion(request, data=request.POST)
        if formulario.is_valid():
            
            user = formulario.get_user()
            
            login(request, user)
            
            return redirect('inicio:inicio')
    else:
        formulario = FormularioDeAutenticacion()
    
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registro(request):
    
    if request.method == "POST":
        formulario = FormularioCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:iniciar_sesion')
    else:
        formulario = FormularioCreacion()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    
    if request.method == "POST":
        formulario = FormularioEdicion(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:perfil')
        
    else:
        formulario = FormularioEdicion(instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})