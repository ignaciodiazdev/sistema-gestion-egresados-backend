from rest_framework.viewsets import ModelViewSet
from educaciones.models import Educacion
from educaciones.api.serializers import EducacionSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EducacionViewSet(ModelViewSet):
    serializer_class = EducacionSerializer
    queryset = Educacion.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'alumno': ['exact'], }
