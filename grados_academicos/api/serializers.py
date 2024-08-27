from rest_framework.serializers import ModelSerializer
from grados_academicos.models import GradoAcademico


class GradoAcademicoSerializer(ModelSerializer):
    class Meta:
        model = GradoAcademico
        fields = '__all__'
