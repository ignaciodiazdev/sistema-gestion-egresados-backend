from rest_framework.viewsets import ModelViewSet
from alumnos_grados.models import AlumnoGrado
from alumnos_grados.api.serializers import AlumnoGradoSerializer


class AlumnoGradoViewSet(ModelViewSet):
    serializer_class = AlumnoGradoSerializer
    queryset = AlumnoGrado.objects.all()
