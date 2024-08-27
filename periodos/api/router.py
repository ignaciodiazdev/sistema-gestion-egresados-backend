from rest_framework.routers import DefaultRouter
from periodos.api.views import PeriodoViewSet

router_periodos = DefaultRouter()

router_periodos.register(
    prefix='periodos',
    viewset=PeriodoViewSet,
    basename='periodos'
)
