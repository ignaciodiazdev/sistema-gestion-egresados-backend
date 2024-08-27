from rest_framework.viewsets import ModelViewSet
from carreras.models import Carrera
from carreras.api.serializers import CarreraSerializer


class CarreraViewSet(ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = Carrera.objects.all()
