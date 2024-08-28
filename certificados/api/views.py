from rest_framework.viewsets import ModelViewSet
from certificados.models import Certificado
from certificados.api.serializers import CertificadoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CertificadoViewSet(ModelViewSet):
    serializer_class = CertificadoSerializer
    queryset = Certificado.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'alumno': ['exact'], }
