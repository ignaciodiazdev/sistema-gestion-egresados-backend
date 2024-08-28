from rest_framework.viewsets import ModelViewSet
from empleos.models import Empleo
from empleos.api.serializers import EmpleoSerializer


class EmpleoViewSet(ModelViewSet):
    serializer_class = EmpleoSerializer
    queryset = Empleo.objects.all()
