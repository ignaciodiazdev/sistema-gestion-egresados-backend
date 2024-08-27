from rest_framework.routers import DefaultRouter
from estados.api.views import EstadoViewSet

router_estados = DefaultRouter()

router_estados.register(
    prefix='estados',
    viewset=EstadoViewSet,
    basename='estados'
)
