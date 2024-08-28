from rest_framework.serializers import ModelSerializer
from educaciones.models import Educacion


class EducacionSerializer(ModelSerializer):
    class Meta:
        model = Educacion
        fields = '__all__'
