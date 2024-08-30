# from rest_framework.viewsets import ModelViewSet
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.response import Response
# from django.contrib.auth.hashers import make_password

# from django.contrib.auth.models import User
# from usuarios.api.serializers import UserSerializer


# class UserApiViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def create(self, request, *args, **kwargs):
#         request.data['password'] = make_password(request.data['password'])
#         return super().create(request, *args, **kwargs)


# class UserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from usuarios.api.serializers import UserSerializer
from rest_framework.response import Response

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, ChangePasswordSerializer
from rest_framework import status


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():  # Asegúrate de validar antes de guardar
            # Guardar la nueva contraseña
            serializer.save()

            return Response({'message': 'La contraseña ha sido cambiada con éxito.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
