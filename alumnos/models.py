from django.db import models
from periodos.models import Periodo
from carreras.models import Carrera
from estados.models import Estado


class Alumno(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=60)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'alumno'
