from rest_framework.serializers import ModelSerializer
from alumnos.models import Alumno
from periodos.api.serializers import PeriodoSerializer
from carreras.api.serializers import CarreraSerializer
from estados.api.serializers import EstadoSerializer


class AlumnoSerializer(ModelSerializer):
    periodo_data = PeriodoSerializer(source='periodo', read_only=True)
    carrera_data = CarreraSerializer(source='carrera', read_only=True)
    estado_data = EstadoSerializer(source='estado', read_only=True)

    class Meta:
        model = Alumno
        fields = '__all__'
