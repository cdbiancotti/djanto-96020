from django.shortcuts import render, redirect
from vehiculos.models import Auto

def listado(request):
    lista = Auto.objects.all()
    return render(request, 'vehiculos/listado.html', {'lista': lista})

# def crear_vehiculo(request, marca, modelo, fecha):
def crear_vehiculo(request):
    
    print('GET >>>>', request.GET)
    print('POST >>>>', request.POST)
    
    if request.method == 'POST':
        auto = Auto(marca=request.POST.get('marca'), modelo=request.POST.get('modelo'), fecha_fabricacion=request.POST.get('fecha_fabricacion'))
        auto.save()
        return redirect('vehiculos:inicio')
    
    return render(request, 'vehiculos/crear.html')