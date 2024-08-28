from rest_framework.viewsets import ModelViewSet
from experiencias.models import Experiencia
from experiencias.api.serializers import ExperienciaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ExperienciaViewSet(ModelViewSet):
    serializer_class = ExperienciaSerializer
    queryset = Experiencia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'alumno': ['exact'], }
