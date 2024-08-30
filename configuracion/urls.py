from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from grados_academicos.api.router import router_grados_academicos
from carreras.api.router import router_carreras
from estados.api.router import router_estados
from periodos.api.router import router_periodos
from alumnos.api.router import router_alumnos
from alumnos_grados.api.router import router_alumnos_grados
# from usuarios.api.router import router_usuarios
from usuarios.api.views import UserView
from alumnos.api.views import AlumnoDetailView
from certificados.api.router import router_certificados
from experiencias.api.router import router_experiencias
from educaciones.api.router import router_educaciones
from empleos.api.router import router_empleos

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/me/', UserView.as_view()),
    path('api/info-alumno/', AlumnoDetailView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router_grados_academicos.urls)),
    path('api/', include(router_carreras.urls)),
    path('api/', include(router_estados.urls)),
    path('api/', include(router_periodos.urls)),
    path('api/', include(router_alumnos.urls)),
    path('api/', include(router_alumnos_grados.urls)),
    # path('api/', include(router_usuarios.urls)),
    path('api/', include(router_certificados.urls)),
    path('api/', include(router_experiencias.urls)),
    path('api/', include(router_educaciones.urls)),
    path('api/', include(router_empleos.urls)),
    # Incluye las rutas de la aplicación de usuarios
    path('api/', include('usuarios.api.router')),
]
