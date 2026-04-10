from django.urls import path
from vehiculos.views import listado, crear_vehiculo

app_name = 'vehiculos'

urlpatterns = [
    path('', listado, name='inicio'),
    # path('crear/<marca>/<modelo>/<fecha>/', crear_vehiculo, name='crear'),
    path('crear/', crear_vehiculo, name='crear'),
]
