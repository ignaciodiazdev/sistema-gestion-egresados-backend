from rest_framework import serializers
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError  # Para cambio de contraseña
# Para cambio de contraseña
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = '__all__'
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extraemos la contraseña
        user = User(**validated_data)
        user.set_password(password)  # Encripta la contraseña
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                "La contraseña actual es incorrecta.")
        return value

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        # Usar .get() en lugar de acceso directo
        new_password = self.validated_data.get('new_password')

        if new_password:
            user.set_password(new_password)
            user.save()
        return user
