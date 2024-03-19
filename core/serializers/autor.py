from rest_framework.serializers import ModelSerializer

from core.models import Autor

class AutorSerializers(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"