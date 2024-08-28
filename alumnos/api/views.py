from rest_framework.viewsets import ModelViewSet
from alumnos.models import Alumno
from alumnos.api.serializers import AlumnoSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Importaciones para obtener datos de un usuario en especifico al hacer login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AlumnoViewSet(ModelViewSet):
    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'codigo': ['exact'], }

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class AlumnoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            alumno = Alumno.objects.get(user=request.user)
            serializer = AlumnoSerializer(alumno)
            return Response(serializer.data)
        except Alumno.DoesNotExist:
            return Response({"detail": "No existe un alumno asociado a este usuario."}, status=404)
