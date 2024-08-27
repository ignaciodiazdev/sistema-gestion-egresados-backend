from rest_framework.serializers import ModelSerializer
from periodos.models import Periodo


class PeriodoSerializer(ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'
