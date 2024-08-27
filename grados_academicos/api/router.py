from rest_framework.routers import DefaultRouter
from grados_academicos.api.views import GradoAcademicoViewSet

router_grados_academicos = DefaultRouter()

router_grados_academicos.register(
    prefix='grados-academicos',
    viewset=GradoAcademicoViewSet,
    basename='grados-academicos'
)
