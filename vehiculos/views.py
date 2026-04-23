from django.shortcuts import render, redirect
from vehiculos.models import Auto
from vehiculos.forms import FormularioCrearAuto, FormularioBusquedaAuto, FormularioModificacionAuto
from django.contrib.auth.decorators import login_required

def listado(request):
    # lista = Auto.objects.all()
    
    formulario = FormularioBusquedaAuto(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data
        lista = Auto.objects.filter(marca__icontains=data.get('marca'),modelo__icontains=data.get('modelo'))
    else:
        lista = Auto.objects.all()
    
    return render(request, 'vehiculos/listado.html', {'lista': lista, 'formulario': formulario})

@login_required
# def crear_vehiculo(request, marca, modelo, fecha):
def crear_vehiculo(request):
    
    # print('GET >>>>', request.GET)
    # print('POST >>>>', request.POST)
    
    if request.method == 'POST':
        formulario = FormularioCrearAuto(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            auto = Auto(marca=data.get('marca'), modelo=data.get('modelo'), fecha_fabricacion=data.get('fecha_fabricacion'), imagen=data.get('imagen'))
            auto.save()
            return redirect('vehiculos:inicio')
    else:
        formulario = FormularioCrearAuto()
    
    return render(request, 'vehiculos/crear.html', {'formulario': formulario})

def detalle_vehiculo(request, identificador):
    
    auto = Auto.objects.get(id=identificador)
    
    return render(request, 'vehiculos/detalle.html', {'auto': auto})

@login_required
def eliminar_vehiculo(request, identificador):
    
    auto = Auto.objects.get(id=identificador)
    auto.delete()
    
    return redirect('vehiculos:inicio')

@login_required
def modificar_vehiculo(request, identificador):
    
    auto = Auto.objects.get(id=identificador)
    
    if request.method == "POST":
        formulario = FormularioModificacionAuto(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            auto.marca = data['marca']
            auto.modelo = data['modelo']
            auto.fecha_fabricacion = data['fecha_fabricacion']
            auto.imagen = data['imagen']
            auto.save()
            return redirect('vehiculos:inicio')
    else:
        formulario = FormularioModificacionAuto(initial={'marca': auto.marca, 'modelo':  auto.modelo, 'fecha_fabricacion': auto.fecha_fabricacion, 'imagen': auto.imagen})
    
    return render(request, 'vehiculos/modificar.html', {'auto': auto, 'formulario': formulario})
            
    