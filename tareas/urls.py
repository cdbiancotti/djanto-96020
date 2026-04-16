from django.urls import path
from tareas.views import tareas, ListaTareas, CrearTarea, ModificarTarea, BorrarTarea, DetalleTarea

app_name = 'tareas'

urlpatterns = [
    path('', ListaTareas.as_view(), name='tareas'),
    path('crear/', CrearTarea.as_view(), name='crear_tarea'),
    path('<pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('<pk>/borrar/', BorrarTarea.as_view(), name='borrar_tarea'),
    path('<pk>/modificar/', ModificarTarea.as_view(), name='modificar_tarea'),
]
