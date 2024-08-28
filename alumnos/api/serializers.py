from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from alumnos.models import Alumno
from periodos.api.serializers import PeriodoSerializer
from carreras.api.serializers import CarreraSerializer
from estados.api.serializers import EstadoSerializer
from django.contrib.auth.models import User


class AlumnoSerializer(ModelSerializer):
    periodo_data = PeriodoSerializer(source='periodo', read_only=True)
    carrera_data = CarreraSerializer(source='carrera', read_only=True)
    estado_data = EstadoSerializer(source='estado', read_only=True)
    user = PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Alumno
        fields = '__all__'

    def update(self, instance, validated_data):
        user_data = validated_data.get('user', None)
        if user_data:
            instance.user = user_data
        instance.save()
        return instance
