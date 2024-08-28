from django.db import models
from alumnos.models import Alumno
# Create your models here.


class Experiencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

    class Meta:
        db_table = 'experiencia_laboral'
