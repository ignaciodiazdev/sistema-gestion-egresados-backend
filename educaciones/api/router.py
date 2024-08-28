from rest_framework.routers import DefaultRouter
from educaciones.api.views import EducacionViewSet

router_educaciones = DefaultRouter()

router_educaciones.register(
    prefix='educaciones',
    viewset=EducacionViewSet,
    basename='educaciones'
)
