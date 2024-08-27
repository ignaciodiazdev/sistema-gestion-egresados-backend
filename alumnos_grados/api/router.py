from rest_framework.routers import DefaultRouter
from alumnos_grados.api.views import AlumnoGradoViewSet

router_alumnos_grados = DefaultRouter()

router_alumnos_grados.register(
    prefix='alumnos-grados',
    viewset=AlumnoGradoViewSet,
    basename='alumnos-grados'
)
