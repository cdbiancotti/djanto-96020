from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)