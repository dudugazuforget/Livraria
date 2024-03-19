from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers import AutorSerializers

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers