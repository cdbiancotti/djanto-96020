from django.contrib import admin
from tareas.models import Tarea


class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'completada', 'fecha_creacion']
    list_filter = ['fecha_creacion']
    search_fields = ['titulo', 'descripcion']

admin.site.register(Tarea, TareaAdmin)