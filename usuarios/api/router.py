from django.urls import path
from rest_framework.routers import DefaultRouter

from usuarios.api.views import UserApiViewSet, UserView


router_usuarios = DefaultRouter()

router_usuarios.register(
    prefix='usuarios', basename='usuarios', viewset=UserApiViewSet
)
# router_usuarios.register(
#     prefix='auth/me/', basename='auth/me/', viewset=UserView.as_view()
# )
# urlpatterns = [
#     path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('auth/me/', UserView.as_view())
# ]
