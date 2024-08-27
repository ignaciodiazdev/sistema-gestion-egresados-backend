from rest_framework.serializers import ModelSerializer
from alumnos_grados.models import AlumnoGrado
from alumnos.api.serializers import AlumnoSerializer
from grados_academicos.api.serializers import GradoAcademicoSerializer


class AlumnoGradoSerializer(ModelSerializer):
    alumno_data = AlumnoSerializer(source='alumno', read_only=True)
    grado_academico_data = GradoAcademicoSerializer(
        source='grado_academico', read_only=True)

    class Meta:
        model = AlumnoGrado
        fields = '__all__'
