from django.contrib.auth.models import AbstractUser
from django.db import models

class Keyboard(models.Model):
    TYPE_CHOICES = [
        ('membrane', 'Membrane'),
        ('mechanical', 'Mechanical'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default = 'membrane')
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.type})"

class UserProfile(AbstractUser):
    username = models.CharField(max_length=30, default='username_not_found')
    nickname = models.CharField(max_length=30)
    favourite_keyboards = models.ForeignKey(Keyboard, on_delete = models.CASCADE)
    pass

# email unique field, sacar por interfaz error si se repiten (checkear la base de datos anets de insertar), no mostrar en actualizacion
# buscar not nullable