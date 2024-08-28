from rest_framework.routers import DefaultRouter
from empleos.api.views import EmpleoViewSet

router_empleos = DefaultRouter()

router_empleos.register(
    prefix='empleos',
    viewset=EmpleoViewSet,
    basename='empleos'
)
