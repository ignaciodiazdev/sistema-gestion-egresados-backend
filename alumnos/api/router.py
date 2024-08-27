from rest_framework.routers import DefaultRouter
from alumnos.api.views import AlumnoViewSet

router_alumnos = DefaultRouter()

router_alumnos.register(
    prefix='alumnos',
    viewset=AlumnoViewSet,
    basename='alumnos'
)
