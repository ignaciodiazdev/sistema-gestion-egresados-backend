from django.db import models

# Create your models here.


class Carrera(models.Model):
    nombre = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'carrera'
