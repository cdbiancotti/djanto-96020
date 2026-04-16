from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=80)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f"Tarea ({self.pk}): {self.titulo}"