from django import forms
from tareas.models import Tarea


class ModificarTareaFormulario(forms.ModelForm):
    # fecha_fabricacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Tarea
        # fields = ['descripcion', 'completada']
        fields = "__all__"
        widgets = {
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'})
        }
        
class BuscarTarea(forms.Form):
    titulo = forms.CharField(max_length=80, required=False)
    completada = forms.BooleanField(required=False)