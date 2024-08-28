from django.db import models
# Create your models here.


class Empleo(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    empresa = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    fecha_expiracion = models.DateField()
    url = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'empleo'
