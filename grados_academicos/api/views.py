from rest_framework.viewsets import ModelViewSet
from grados_academicos.models import GradoAcademico
from grados_academicos.api.serializers import GradoAcademicoSerializer


class GradoAcademicoViewSet(ModelViewSet):
    serializer_class = GradoAcademicoSerializer
    queryset = GradoAcademico.objects.all()
