from rest_framework.routers import DefaultRouter
from certificados.api.views import CertificadoViewSet

router_certificados = DefaultRouter()

router_certificados.register(
    prefix='certificados',
    viewset=CertificadoViewSet,
    basename='certificados'
)
