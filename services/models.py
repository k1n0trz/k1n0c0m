from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.user.username

solicitud_select = [
    (1, 'Seleccione un servicio'),
    (2, 'Marketing'),
    (3, 'Diseño Gráfico'),
    (4, 'Desarrollo Web'),
    (5, 'Producción Fotográfica/Audiovisual'),
    (6, 'Tecnología Blockchain'),
    (7, 'Otros...'),
]

class Solicitud(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    contrato = models.IntegerField(null=False, blank=False, choices=solicitud_select, default=1)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre