from rest_framework.routers import DefaultRouter
from experiencias.api.views import ExperienciaViewSet

router_experiencias = DefaultRouter()

router_experiencias.register(
    prefix='experiencias',
    viewset=ExperienciaViewSet,
    basename='experiencias'
)
