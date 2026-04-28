from django.db import models


class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='autos', null=True, blank=True)
    fecha_fabricacion = models.DateField()

    def __str__(self):
        return f'Auto: {self.marca} {self.modelo}'