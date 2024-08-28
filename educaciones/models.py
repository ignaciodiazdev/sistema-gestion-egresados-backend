from django.db import models
from alumnos.models import Alumno

# Create your models here.


class Educacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    institucion = models.CharField(max_length=255)
    carrera = models.CharField(max_length=100, default="No Registrado")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    tipo_estudio = models.CharField(max_length=60, default="No Registrado")

    def __str__(self):
        return f"{self.institucion} - {self.carrera}"

    class Meta:
        db_table = 'formacion_academica'
