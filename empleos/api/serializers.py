from rest_framework.serializers import ModelSerializer
from empleos.models import Empleo


class EmpleoSerializer(ModelSerializer):
    class Meta:
        model = Empleo
        fields = '__all__'
