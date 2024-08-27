from rest_framework.viewsets import ModelViewSet
from alumnos.models import Alumno
from alumnos.api.serializers import AlumnoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AlumnoViewSet(ModelViewSet):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'codigo': ['exact'], }
