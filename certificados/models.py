from django.db import models
from alumnos.models import Alumno
# Create your models here.


class Certificado(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    entidad_emisora = models.CharField(max_length=255)
    fecha_emision = models.DateField()
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'certificado'
