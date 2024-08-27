from rest_framework.viewsets import ModelViewSet
from periodos.models import Periodo
from periodos.api.serializers import PeriodoSerializer


class PeriodoViewSet(ModelViewSet):
    serializer_class = PeriodoSerializer
    queryset = Periodo.objects.all()
