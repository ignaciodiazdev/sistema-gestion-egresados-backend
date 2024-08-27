from rest_framework.viewsets import ModelViewSet
from estados.models import Estado
from estados.api.serializers import EstadoSerializer


class EstadoViewSet(ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
