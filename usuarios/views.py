from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def iniciar_sesion(request):
    
    formulario = AuthenticationForm()
    
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})
