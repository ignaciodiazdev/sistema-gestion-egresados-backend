from rest_framework.serializers import ModelSerializer
from experiencias.models import Experiencia


class ExperienciaSerializer(ModelSerializer):
    class Meta:
        model = Experiencia
        fields = '__all__'
