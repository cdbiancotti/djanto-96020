from django.urls import path
from vehiculos.views import listado, crear_vehiculo, detalle_vehiculo, eliminar_vehiculo, modificar_vehiculo

app_name = 'vehiculos'

urlpatterns = [
    path('', listado, name='inicio'),
    # path('crear/<marca>/<modelo>/<fecha>/', crear_vehiculo, name='crear'),
    path('crear/', crear_vehiculo, name='crear'),
    path('<identificador>/', detalle_vehiculo, name='detalle'),
    path('<identificador>/eliminar/', eliminar_vehiculo, name='eliminar'),
    path('<identificador>/modificar/', modificar_vehiculo, name='modificar'),
]
