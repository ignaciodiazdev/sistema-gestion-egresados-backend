from rest_framework.serializers import ModelSerializer
from carreras.models import Carrera


class CarreraSerializer(ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'
