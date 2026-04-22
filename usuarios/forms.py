from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class FormularioDeAutenticacion(AuthenticationForm):
    username = forms.CharField(label="Nombre Usuario")
    password = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    
class FormularioCreacion(UserCreationForm):
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir Contrasenia", widget=forms.PasswordInput())
    
    
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            # 'first_name', 
            # 'last_name',
            'password1', 
            'password2'
        ]
        labels = {
            'username': 'Nombre de ususario', 
            # 'first_name': 'Nombre', 
            # 'last_name': 'Apellido', 
            'email': 'Email',
        }
        # help_texts = {
        #     'username': '', 
        # }
        help_texts = { key: '' for key in fields }
        
class FormularioEdicion(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre', 
            'last_name': 'Apellido', 
            'email': 'Email',
        }