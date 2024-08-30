# from django.urls import path
# from rest_framework.routers import DefaultRouter

# from usuarios.api.views import UserApiViewSet, UserView


# router_usuarios = DefaultRouter()

# router_usuarios.register(
#     prefix='usuarios', basename='usuarios', viewset=UserApiViewSet
# )

# ================== LO DE ACA ABAJO SIEMPRE ESTUVO COMENTADO!!! ==================
# router_usuarios.register(
#     prefix='auth/me/', basename='auth/me/', viewset=UserView.as_view()
# )
# urlpatterns = [
#     path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('auth/me/', UserView.as_view())
# ]
# ================== ===============================================================
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, ChangePasswordView

urlpatterns = [
    path('usuarios/', UserListCreateView.as_view(), name='user-list-create'),
    path('usuarios/<int:pk>/',
         UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('usuarios/cambiar-password/',
         ChangePasswordView.as_view(), name='change-password'),
]
