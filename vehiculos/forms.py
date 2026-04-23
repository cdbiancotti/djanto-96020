from django import forms


class FormularioBaseAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=30)
    imagen = forms.ImageField(required=False)
    fecha_fabricacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class FormularioCrearAuto(FormularioBaseAuto):
    ...
    
    
class FormularioModificacionAuto(FormularioBaseAuto):
    ...
    
    
class FormularioBusquedaAuto(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=30, required=False)