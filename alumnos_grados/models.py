from django.db import models
from alumnos.models import Alumno
from grados_academicos.models import GradoAcademico


class AlumnoGrado(models.Model):
    codigo_modular = models.CharField(max_length=50, unique=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    grado_academico = models.ForeignKey(
        GradoAcademico, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.alumno.nombre + " - " + self.grado_academico.nombre

    class Meta:
        db_table = 'alumno_grado'
