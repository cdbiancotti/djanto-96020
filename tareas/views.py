from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tareas.models import Tarea
from django.urls import reverse_lazy
from tareas.forms import ModificarTareaFormulario, BuscarTarea
from django.contrib.auth.mixins import LoginRequiredMixin

def tareas(request):
    return render(request, 'tareas/lista.html')

class ListaTareas(ListView):
    model = Tarea
    template_name = "tareas/lista.html"
    context_object_name = 'tareas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BuscarTarea()
        return context
    
    def get_queryset(self):
        tareas = super().get_queryset()
        formulario = BuscarTarea(self.request.GET)
        if formulario.is_valid():
            
            titulo_a_buscar = formulario.cleaned_data.get('titulo')
            completada_a_buscar = formulario.cleaned_data.get('completada')
            
            tareas = tareas.filter(titulo__icontains=titulo_a_buscar, completada=completada_a_buscar)
        
        return tareas
    

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = "tareas/crear.html"
    fields = ['titulo', 'descripcion', 'fecha_creacion']
    # fields = ['titulo', 'descripcion', 'completada', 'fecha_creacion']
    # fields = "__all__"
    success_url = reverse_lazy("tareas:tareas")


class ModificarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name = "tareas/modificar.html"
    form_class = ModificarTareaFormulario
    success_url = reverse_lazy("tareas:tareas")


class BorrarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "tareas/borrar.html"
    success_url = reverse_lazy("tareas:tareas")


class DetalleTarea(DetailView):
    model = Tarea
    template_name = "tareas/detalle.html"
