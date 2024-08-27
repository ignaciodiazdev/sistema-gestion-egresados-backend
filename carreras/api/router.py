from rest_framework.routers import DefaultRouter
from carreras.api.views import CarreraViewSet

router_carreras = DefaultRouter()

router_carreras.register(
    prefix='carreras',
    viewset=CarreraViewSet,
    basename='carreras'
)
