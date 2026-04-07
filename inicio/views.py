from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# HttpResponse
# def inicio(request):
#     return HttpResponse('<h1>Bienvenidos a mi pagina!</h1>')

# Template con open
# def inicio(request):
#     archivo_abierto = open(r'C:\Users\cdbia\Desktop\96020\django-96020\templates\inicio.html')
#     contenido = archivo_abierto.read()
#     archivo_abierto.close()
#     template = Template(contenido)
#     fecha_hora = datetime.now()
#     contexto = Context({'fecha_hora': fecha_hora})
#     template_renderizado = template.render(contexto)
#     return HttpResponse(template_renderizado)

# Template con loader
# def inicio(request):
#     template = loader.get_template('inicio.html')
#     fecha_hora = datetime.now()
#     template_renderizado = template.render({'fecha_hora': fecha_hora})
#     return HttpResponse(template_renderizado)

# Template con render
def inicio(request):
    
    fecha_hora = datetime.now()
    
    # return render(request, 'inicio.html')
    # return render(request, 'inicio.html', {})
    return render(request, 'inicio.html', {'fecha_hora': fecha_hora})

def vista2(request):
    
    listado = list(range(1, 11))
    
    return render(request, 'condicional_y_bucle.html', {'datos': listado})