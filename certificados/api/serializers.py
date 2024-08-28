from rest_framework.serializers import ModelSerializer
from certificados.models import Certificado


class CertificadoSerializer(ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'
