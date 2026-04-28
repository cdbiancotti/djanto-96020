from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import FormularioDeAutenticacion, FormularioCreacion, FormularioEdicion, CambiarContraseniaFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = FormularioDeAutenticacion(request, data=request.POST)
        if formulario.is_valid():
            
            user = formulario.get_user()
            
            login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
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
    
    info_extra = request.user.infoextra
    
    if request.method == "POST":
        formulario = FormularioEdicion(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            
            # info_extra.avatar = formulario.cleaned_data.get('avatar')
            
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            
            if formulario.cleaned_data.get('fecha_nacimiento'):
                info_extra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            
            info_extra.save()
            formulario.save()
            return redirect('usuarios:perfil')
        
    else:
        formulario = FormularioEdicion(instance=request.user, initial={'fecha_nacimiento': info_extra.fecha_nacimiento, 'avatar': info_extra.avatar })
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class CambioContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambio_contrasenia.html'
    success_url = reverse_lazy('usuarios:perfil')
    form_class = CambiarContraseniaFormulario